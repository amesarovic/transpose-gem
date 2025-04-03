
from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *


class AmmTranspose2(ComponentSpec):
    name: str = "AmmTranspose2"
    category: str = "Transform"

    def optimizeCode(self) -> bool:
        # Return whether code optimization is enabled for this component
        return True

    @dataclass(frozen=True)
    class AmmTranspose2Properties(ComponentProperties):
        pivot_column: SString = SString("pivot column")
        key_columns: list[str] = field(default_factory=list)
        value_columns: list[str] = field(default_factory=list)

    def dialog(self) -> Dialog:
        return Dialog("Transpose").addElement(
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

    def validate(self, context: WorkflowContext, component: Component[AmmTranspose2Properties]) -> List[Diagnostic]:
        # Validate the component's state
        return []

    def _todo_validate(self, context: WorkflowContext, component: Component[AmmTranspose2Properties]) -> List[Diagnostic]:
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

    def onChange(self, context: WorkflowContext, oldState: Component[AmmTranspose2Properties], newState: Component[AmmTranspose2Properties]) -> Component[
    AmmTranspose2Properties]:
        # Handle changes in the component's state and return the new state
        return newState

    import pyspark.sql.functions as F
    
    def foo(df):
        return df.limit(6)

    class AmmTranspose2Code(ComponentCode):
        def __init__(self, newProps):
            self.props: AmmTranspose2.AmmTranspose2Properties = newProps

        def OLD_apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            def bar(df):
                return df.limit(5)

            print(">> key_columns.1:", self.props.key_columns)
            print(">> value_columns.1:", self.props.value_columns)

            key_columns = [ "products" ]
            value_columns = [ "small", "medium", "large" ]
            print(">> key_columns.2:", key_columns)
            print(">> value_columns.2:", value_columns)
            return bar(in0)
            #return self.transpose_df2(in0, key_columns, value_columns)

        def _apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            return in0
            
        def apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            #print(">> Hello Transpose")
            print(">> key_columns.0:", self.props.key_columns)
            print(">> value_columns.0:", self.props.value_columns)
        
            key_columns = [ "products" ]
            value_columns = [ "small", "medium", "large" ]
            print(">> key_columns.1:", key_columns)
            print(">> value_columns.1:", value_columns)

            name_col = "name",
            value_col = "value"
            df = in0
 
            print(">> Hello Transpose")
            # NOTE: optimizer doesn't yet support list comprehension
            available_data_columns = []
            for col_name in value_columns:
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
 
            print(">> END")
            #print(">> transposed_df:", transposed_df.count())
            return transposed_df
