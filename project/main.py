from langgraph.graph import StateGraph

from models.state import GraphState

from graph import graph

from utils.case_manager import save_case


result = graph.invoke(
    {
        "user_input":
        """
        We are a medium-sized retail company.

        We use Excel, SQL Server and Power BI.

        Different departments produce conflicting reports.

        Customer information is duplicated across systems.

        Data ownership is unclear.

        We do not have a data catalog.

        Business definitions vary among departments.

        Data quality problems are recurrent and require manual corrections.

        We lack formal governance processes.
        """
    }
)

save_case(result)

print(result)

print("RETRIEVED KNOWLEDGE")

for chunk in result[
    "retrieved_knowledge"
]:

    print()

    print("-" * 80)

    print(chunk[:500])

    print()

print("=" * 80)
print("DIAGNOSIS")
print("=" * 80)

print(
    result["diagnosis"]
)

print(result["technology_profile"])
print(result["strategy"])
print(result["final_response"])