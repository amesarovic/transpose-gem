# Using original normal list comprehension

from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *

class TransposeNoOpt(ComponentSpec):
    name: str = "TransposeNoOpt"
    category: str = "Transform"

    def optimizeCode(self) -> bool:
        return False

    @dataclass(frozen=True)
    class TransposeNoOptProperties(ComponentProperties):
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

    def validate(self, context: WorkflowContext, component: Component[TransposeNoOptProperties]) -> List[Diagnostic]:
        diagnostics = []
        if len(component.properties.key_columns) == 0:
             diagnostics.append(
                Diagnostic("properties.key_columns", "At least one key column has to be specified", SeverityLevelEnum.Error))
        if len(component.properties.value_columns) == 0:
             diagnostics.append(
                Diagnostic("properties.value_columns", "At least one value column has to be specified", SeverityLevelEnum.Error))
        common = list(set(component.properties.key_columns).intersection(component.properties.value_columns))
        if common:
            diagnostics.append(
                Diagnostic(f"properties.value_columns", f"Key and value columns cannot overlap: {common}", SeverityLevelEnum.Error))
        return diagnostics

    def onChange(self, context: WorkflowContext, oldState: Component[TransposeNoOptProperties], newState: Component[TransposeNoOptProperties]) -> Component[
    TransposeNoOptProperties]:
        return newState

    class TransposeNoOptCode(ComponentCode):
        def __init__(self, newProps):
            self.props: TransposeNoOpt.TransposeNoOptProperties = newProps

        def apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            import pyspark.sql.functions as F

            data_columns = [col_name for col_name in self.props.value_columns if col_name in in0.columns]

            dfs = [
                in0.select([F.col(key_col) for key_col in self.props.key_columns] +
                        [F.lit(data_col_name).cast("string").alias("Name"),
                         F.col(data_col_name).cast("string").alias("Value")])
                for data_col_name in data_columns ]
            
            transposed_df = dfs[0]
            for df in dfs[1:]:
                transposed_df = transposed_df.union(df)
 
            return transposed_df