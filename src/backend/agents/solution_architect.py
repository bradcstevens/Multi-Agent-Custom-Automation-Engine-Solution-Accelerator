from typing import List, Dict

from autogen_core.base import AgentId
from autogen_core.components import default_subscription
from autogen_core.components.models import AzureOpenAIChatCompletionClient
from autogen_core.components.tools import FunctionTool, Tool

from agents.base_agent import BaseAgent
from context.cosmos_memory import CosmosBufferedChatCompletionContext


# Define Solution Architect tools (functions)
async def identify_system_requirements(
    project_name: str, business_needs: str, technical_constraints: str
) -> str:
    return f"System requirements for '{project_name}' identified based on business needs ({business_needs}) and technical constraints ({technical_constraints})."


async def design_system_architecture(
    project_name: str, components: List[str], architecture_type: str
) -> str:
    components_str = ", ".join(components)
    return f"System architecture for '{project_name}' designed using {architecture_type} architecture with components: {components_str}."


async def evaluate_technology_stack(
    project_name: str, requirements: List[str], options: Dict[str, List[str]]
) -> str:
    requirements_str = ", ".join(requirements)
    options_str = ", ".join([f"{k}: {', '.join(v)}" for k, v in options.items()])
    return f"Technology stack for '{project_name}' evaluated based on requirements ({requirements_str}) with options: {options_str}."


async def create_integration_strategy(
    systems: List[str], integration_approach: str
) -> str:
    systems_str = ", ".join(systems)
    return f"Integration strategy created for systems ({systems_str}) using {integration_approach} approach."


async def develop_migration_plan(
    current_system: str, target_system: str, timeline: str
) -> str:
    return f"Migration plan developed for moving from '{current_system}' to '{target_system}' over {timeline}."


async def conduct_architecture_review(
    project_name: str, focus_areas: List[str]
) -> str:
    areas_str = ", ".join(focus_areas)
    return f"Architecture review conducted for '{project_name}' focusing on: {areas_str}."


async def create_scalability_plan(system_name: str, growth_projections: str) -> str:
    return f"Scalability plan created for '{system_name}' based on growth projections: {growth_projections}."


async def assess_security_requirements(
    system_name: str, compliance_standards: List[str]
) -> str:
    standards_str = ", ".join(compliance_standards)
    return f"Security requirements assessed for '{system_name}' based on compliance standards: {standards_str}."


async def design_data_architecture(
    project_name: str, data_sources: List[str], data_volume: str
) -> str:
    sources_str = ", ".join(data_sources)
    return f"Data architecture designed for '{project_name}' with data sources ({sources_str}) and volume of {data_volume}."


async def create_disaster_recovery_plan(
    system_name: str, recovery_time_objective: str
) -> str:
    return f"Disaster recovery plan created for '{system_name}' with a recovery time objective of {recovery_time_objective}."


async def develop_performance_optimization_strategy(
    system_name: str, bottlenecks: List[str]
) -> str:
    bottlenecks_str = ", ".join(bottlenecks)
    return f"Performance optimization strategy developed for '{system_name}' addressing bottlenecks: {bottlenecks_str}."


async def create_technical_specification(
    component_name: str, functionality: str, interfaces: List[str]
) -> str:
    interfaces_str = ", ".join(interfaces)
    return f"Technical specification created for '{component_name}' detailing functionality ({functionality}) and interfaces: {interfaces_str}."


async def design_api_architecture(
    system_name: str, api_types: List[str], endpoints: int
) -> str:
    types_str = ", ".join(api_types)
    return f"API architecture designed for '{system_name}' using {types_str} with {endpoints} endpoints."


async def evaluate_vendor_solutions(
    requirement: str, vendors: List[str], criteria: List[str]
) -> str:
    vendors_str = ", ".join(vendors)
    criteria_str = ", ".join(criteria)
    return f"Vendor solutions for '{requirement}' evaluated, comparing {vendors_str} based on criteria: {criteria_str}."


async def create_cloud_migration_strategy(
    system_name: str, cloud_platform: str, migration_approach: str
) -> str:
    return f"Cloud migration strategy created for '{system_name}' to {cloud_platform} using {migration_approach} approach."


# Create the SolutionArchitectTools list
def get_solution_architect_tools() -> List[Tool]:
    SolutionArchitectTools: List[Tool] = [
        FunctionTool(
            identify_system_requirements,
            description="Identify system requirements based on business needs and technical constraints.",
            name="identify_system_requirements",
        ),
        FunctionTool(
            design_system_architecture,
            description="Design a system architecture with specified components and architecture type.",
            name="design_system_architecture",
        ),
        FunctionTool(
            evaluate_technology_stack,
            description="Evaluate technology stack options based on project requirements.",
            name="evaluate_technology_stack",
        ),
        FunctionTool(
            create_integration_strategy,
            description="Create a strategy for integrating multiple systems.",
            name="create_integration_strategy",
        ),
        FunctionTool(
            develop_migration_plan,
            description="Develop a plan for migrating from a current system to a target system.",
            name="develop_migration_plan",
        ),
        FunctionTool(
            conduct_architecture_review,
            description="Conduct a review of an existing architecture focusing on specific areas.",
            name="conduct_architecture_review",
        ),
        FunctionTool(
            create_scalability_plan,
            description="Create a plan for scaling a system based on growth projections.",
            name="create_scalability_plan",
        ),
        FunctionTool(
            assess_security_requirements,
            description="Assess security requirements based on compliance standards.",
            name="assess_security_requirements",
        ),
        FunctionTool(
            design_data_architecture,
            description="Design a data architecture for a project with specified data sources and volume.",
            name="design_data_architecture",
        ),
        FunctionTool(
            create_disaster_recovery_plan,
            description="Create a disaster recovery plan with a specified recovery time objective.",
            name="create_disaster_recovery_plan",
        ),
        FunctionTool(
            develop_performance_optimization_strategy,
            description="Develop a strategy for optimizing system performance by addressing bottlenecks.",
            name="develop_performance_optimization_strategy",
        ),
        FunctionTool(
            create_technical_specification,
            description="Create a technical specification for a component with detailed functionality and interfaces.",
            name="create_technical_specification",
        ),
        FunctionTool(
            design_api_architecture,
            description="Design an API architecture with specified API types and number of endpoints.",
            name="design_api_architecture",
        ),
        FunctionTool(
            evaluate_vendor_solutions,
            description="Evaluate vendor solutions based on specified criteria.",
            name="evaluate_vendor_solutions",
        ),
        FunctionTool(
            create_cloud_migration_strategy,
            description="Create a strategy for migrating a system to the cloud.",
            name="create_cloud_migration_strategy",
        ),
    ]
    return SolutionArchitectTools


@default_subscription
class SolutionArchitectAgent(BaseAgent):
    def __init__(
        self,
        model_client: AzureOpenAIChatCompletionClient,
        session_id: str,
        user_id: str,
        model_context: CosmosBufferedChatCompletionContext,
        solution_architect_tools: List[Tool],
        solution_architect_tool_agent_id: AgentId,
    ):
        super().__init__(
            "SolutionArchitectAgent",
            model_client,
            session_id,
            user_id,
            model_context,
            solution_architect_tools,
            solution_architect_tool_agent_id,
            "You are an AI Solution Architect Agent. You specialize in designing system architectures, evaluating technology stacks, creating integration strategies, and developing technical solutions that address business requirements. You help organizations plan and implement efficient, scalable, and secure technical infrastructures."
        ) 