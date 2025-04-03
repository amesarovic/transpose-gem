from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *


class AmmTest_01(ComponentSpec):
    name: str = "AmmTest_01"
    category: str = "Transform"

    def optimizeCode(self) -> bool:
        # Return whether code optimization is enabled for this component
        return True

    @dataclass(frozen=True)
    class AmmTest_01Properties(ComponentProperties):
        # properties for the component with default values
        my_property: SString = SString("default value of my property")

    def _dialog(self) -> Dialog:
        # Define the UI dialog structure for the component
        return Dialog("AmmTest_01")

    def _dialog(self) -> Dialog:
        return Dialog("Transpose").addElement(
            ColumnsLayout(gap="1rem", height="100%")
                .addColumn(Ports(), "content")
                .addColumn(
                StackLayout(height="100%").addElement(ColumnsLayout("1rem")
                    .addElement(
                        ColumnsLayout("1rem").addColumn(
                            SchemaColumnsDropdown("Key columns")
                                .withMultipleSelection()
                                .bindSchema("component.ports.inputs[0].schema")
                                .bindProperty("key_columns")
                                .showErrorsFor("key_columns"),
                            "5fr",
                    ))
                    .addElement(TitleElement("Title"))
                    .addElement(
                        ColumnsLayout("1rem").addColumn(
                            SchemaColumnsDropdown("Key columns")
                                .withMultipleSelection()
                                .bindSchema("component.ports.inputs[0].schema")
                                .bindProperty("key_columns")
                                .showErrorsFor("key_columns_columns"),
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
        )

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

    def _dialog(self) -> Dialog:
        return Dialog("ColumnParser").addElement(
            ColumnsLayout(gap="1rem", height="100%")
            .addColumn(Ports(), "content")
            .addColumn(
                StackLayout(height="100%")
                    .addElement(TitleElement("elt_1"))
                    .addElement(TitleElement("elt_2"))
                    .addElement(TitleElement("elt_3"))
            )
        )
        

    def validate(self, context: WorkflowContext, component: Component[AmmTest_01Properties]) -> List[Diagnostic]:
        # Validate the component's state
        return []

    def onChange(self, context: WorkflowContext, oldState: Component[AmmTest_01Properties], newState: Component[AmmTest_01Properties]) -> Component[
    AmmTest_01Properties]:
        # Handle changes in the component's state and return the new state
        return newState


    class AmmTest_01Code(ComponentCode):
        def __init__(self, newProps):
            self.props: AmmTest_01.AmmTest_01Properties = newProps

        def apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            # This method contains logic used to generate the spark code from the given inputs.
            return in0

