
from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *


class AndreTranspose(ComponentSpec):
    name: str = "AndreTranspose2"
    category: str = "Transform"

    def optimizeCode(self) -> bool:
        # Return whether code optimization is enabled for this component
        return True

    @dataclass(frozen=True)
    class AndreTransposeProperties(ComponentProperties):
        # properties for the component with default values
        pivot_column: SString = SString("pivot column")
        key_columns: list[str] = field(default_factory=list)
        value_columns: list[str] = field(default_factory=list)

    def dialog(self) -> Dialog:
        return Dialog("ColumnParser").addElement(
            ColumnsLayout(gap="1rem", height="100%")
            .addColumn(Ports(), "content")
            .addColumn(
                StackLayout(height="100%")
                    .addElement(
                        ColumnsLayout("1rem").addColumn(
                            SchemaColumnsDropdown("Key columns")
                                .withMultipleSelection()
                                .bindSchema("component.ports.inputs[0].schema")
                                .bindProperty("key_columns")
                                .showErrorsFor("key_columns"),
                            "5fr",
                    ))
                    .addElement(
                        ColumnsLayout("1rem").addColumn(
                            SchemaColumnsDropdown("Value columns")
                                .withMultipleSelection()
                                .bindSchema("component.ports.inputs[0].schema")
                                .bindProperty("value_columns")
                                .showErrorsFor("value_columns"),
                            "5fr",
                    ))
            )
        )

    



    def validate(self, context: WorkflowContext, component: Component[AndreTransposeProperties]) -> List[Diagnostic]:
        # Validate the component's state
        return []

    def _todo_validate(self, context: WorkflowContext, component: Component[AndreTransposeProperties]) -> List[Diagnostic]:
        diagnostics = []
        pivotColMsgDiag = "Pivot column"
        if component.properties.limit.diagnosticMessages is not None and len(component.properties.limit.diagnosticMessages) > 0:
            for message in component.properties.pivot_column.diagnosticMessages:
                diagnostics.append(Diagnostic("properties.pivot_column", message, SeverityLevelEnum.Error))
        else:
            resolved = component.properties.limit.value
            if resolved <= 0:
                diagnostics.append(Diagnostic("properties.pivot_column", pivotColMsgDiag, SeverityLevelEnum.Error))
            else:
                pass
        return diagnostics

    def onChange(self, context: WorkflowContext, oldState: Component[AndreTransposeProperties], newState: Component[AndreTransposeProperties]) -> Component[
    AndreTransposeProperties]:
        # Handle changes in the component's state and return the new state
        return newState

    import pyspark.sql.functions as F
    
    class AndreTransposeCode(ComponentCode):
        def __init__(self, newProps):
            self.props: AndreTranspose.AndreTransposeProperties = newProps

        def apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            # This method contains logic used to generate the spark code from the given inputs.
            pivot_col = "products" # TODO: make configurable
            columns = ["small", "medium"] # TODO: ibid
            return self.transpose_df(in0, [pivot_col], columns)

        def transpose_df(self,
                df: DataFrame,
                key_columns: list[str],
                data_columns: list[str],
                name_col: str = "name",
                value_col: str = "value"
            ) -> DataFrame:

            available_data_columns = []
            for col_name in data_columns:
                if col_name in df.columns:
                    available_data_columns.append(col_name)

            dfs = []
            for data_col_name in available_data_columns:
                selected_df = df.select([F.col(key_col) for key_col in key_columns] +
                                [F.lit(data_col_name).cast("string").alias(name_column),
                                 F.col(data_col_name).cast("string").alias(value_column)])
                dfs.append(selected_df)

            transposed_df = dfs[0]
            for other_df in dfs[1:]:
                transposed_df = transposed_df.union(other_df)

            return transposed_df
