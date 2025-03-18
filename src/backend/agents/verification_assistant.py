from typing import List, Dict

from autogen_core.base import AgentId
from autogen_core.components import default_subscription
from autogen_core.components.models import AzureOpenAIChatCompletionClient
from autogen_core.components.tools import FunctionTool, Tool

from agents.base_agent import BaseAgent
from context.cosmos_memory import CosmosBufferedChatCompletionContext


# Define Verification Assistant tools (functions)
async def review_requirements(
    project_name: str, requirements_list: List[str]
) -> str:
    requirements_str = ", ".join(requirements_list)
    return f"Requirements for '{project_name}' reviewed: {requirements_str}."


async def validate_solution_architecture(
    project_name: str, architecture_components: List[str], validation_criteria: List[str]
) -> str:
    components_str = ", ".join(architecture_components)
    criteria_str = ", ".join(validation_criteria)
    return f"Solution architecture for '{project_name}' validated against criteria ({criteria_str}) for components: {components_str}."


async def perform_security_assessment(
    system_name: str, security_aspects: List[str], risk_level: str
) -> str:
    aspects_str = ", ".join(security_aspects)
    return f"Security assessment performed for '{system_name}' examining aspects ({aspects_str}) with identified risk level: {risk_level}."


async def conduct_performance_review(
    system_name: str, performance_metrics: List[str], benchmark_results: Dict[str, str]
) -> str:
    metrics_str = ", ".join(performance_metrics)
    benchmark_str = ", ".join([f"{k}: {v}" for k, v in benchmark_results.items()])
    return f"Performance review conducted for '{system_name}' measuring metrics ({metrics_str}) with benchmark results: {benchmark_str}."


async def verify_compliance(
    system_name: str, compliance_standards: List[str], compliance_status: str
) -> str:
    standards_str = ", ".join(compliance_standards)
    return f"Compliance verification completed for '{system_name}' against standards ({standards_str}) with status: {compliance_status}."


async def review_documentation(
    document_name: str, document_type: str, quality_level: str
) -> str:
    return f"Documentation review completed for '{document_name}' of type {document_type} with quality assessed as: {quality_level}."


async def validate_test_coverage(
    system_name: str, test_types: List[str], coverage_percentage: float
) -> str:
    types_str = ", ".join(test_types)
    return f"Test coverage validated for '{system_name}' including test types ({types_str}) with {coverage_percentage}% coverage."


async def perform_code_review(
    component_name: str, code_quality_metrics: List[str], issues_found: int
) -> str:
    metrics_str = ", ".join(code_quality_metrics)
    return f"Code review performed for '{component_name}' assessing metrics ({metrics_str}) with {issues_found} issues identified."


async def validate_integration_points(
    system_name: str, integration_points: List[str], test_results: str
) -> str:
    points_str = ", ".join(integration_points)
    return f"Integration points validated for '{system_name}' including ({points_str}) with test results: {test_results}."


async def review_deployment_plan(
    project_name: str, deployment_stages: List[str], risk_assessment: str
) -> str:
    stages_str = ", ".join(deployment_stages)
    return f"Deployment plan reviewed for '{project_name}' covering stages ({stages_str}) with risk assessment: {risk_assessment}."


async def verify_data_integrity(
    system_name: str, data_types: List[str], integrity_test_results: str
) -> str:
    types_str = ", ".join(data_types)
    return f"Data integrity verified for '{system_name}' including data types ({types_str}) with test results: {integrity_test_results}."


async def conduct_usability_assessment(
    system_name: str, user_personas: List[str], usability_score: float
) -> str:
    personas_str = ", ".join(user_personas)
    return f"Usability assessment conducted for '{system_name}' using personas ({personas_str}) with usability score: {usability_score}/10."


async def review_disaster_recovery_plan(
    system_name: str, scenario_types: List[str], recovery_time_assessment: str
) -> str:
    scenarios_str = ", ".join(scenario_types)
    return f"Disaster recovery plan reviewed for '{system_name}' covering scenarios ({scenarios_str}) with recovery time assessment: {recovery_time_assessment}."


async def perform_scalability_validation(
    system_name: str, load_scenarios: List[str], scaling_capabilities: str
) -> str:
    scenarios_str = ", ".join(load_scenarios)
    return f"Scalability validation performed for '{system_name}' under scenarios ({scenarios_str}) with assessed capabilities: {scaling_capabilities}."


async def verify_business_requirements_alignment(
    project_name: str, business_objectives: List[str], alignment_assessment: str
) -> str:
    objectives_str = ", ".join(business_objectives)
    return f"Alignment with business requirements verified for '{project_name}' against objectives ({objectives_str}) with assessment: {alignment_assessment}."


# Create the VerificationAssistantTools list
def get_verification_assistant_tools() -> List[Tool]:
    VerificationAssistantTools: List[Tool] = [
        FunctionTool(
            review_requirements,
            description="Review requirements for a project to ensure clarity and completeness.",
            name="review_requirements",
        ),
        FunctionTool(
            validate_solution_architecture,
            description="Validate a solution architecture against specified criteria.",
            name="validate_solution_architecture",
        ),
        FunctionTool(
            perform_security_assessment,
            description="Perform a security assessment on a system examining specified aspects.",
            name="perform_security_assessment",
        ),
        FunctionTool(
            conduct_performance_review,
            description="Conduct a performance review of a system based on specified metrics.",
            name="conduct_performance_review",
        ),
        FunctionTool(
            verify_compliance,
            description="Verify compliance of a system with specified standards.",
            name="verify_compliance",
        ),
        FunctionTool(
            review_documentation,
            description="Review documentation for quality and completeness.",
            name="review_documentation",
        ),
        FunctionTool(
            validate_test_coverage,
            description="Validate test coverage for a system across different test types.",
            name="validate_test_coverage",
        ),
        FunctionTool(
            perform_code_review,
            description="Perform a code review based on quality metrics.",
            name="perform_code_review",
        ),
        FunctionTool(
            validate_integration_points,
            description="Validate integration points in a system with test results.",
            name="validate_integration_points",
        ),
        FunctionTool(
            review_deployment_plan,
            description="Review a deployment plan for risks and completeness.",
            name="review_deployment_plan",
        ),
        FunctionTool(
            verify_data_integrity,
            description="Verify data integrity across specified data types.",
            name="verify_data_integrity",
        ),
        FunctionTool(
            conduct_usability_assessment,
            description="Conduct a usability assessment for different user personas.",
            name="conduct_usability_assessment",
        ),
        FunctionTool(
            review_disaster_recovery_plan,
            description="Review a disaster recovery plan for different scenarios.",
            name="review_disaster_recovery_plan",
        ),
        FunctionTool(
            perform_scalability_validation,
            description="Perform scalability validation under different load scenarios.",
            name="perform_scalability_validation",
        ),
        FunctionTool(
            verify_business_requirements_alignment,
            description="Verify alignment with business requirements and objectives.",
            name="verify_business_requirements_alignment",
        ),
    ]
    return VerificationAssistantTools


@default_subscription
class VerificationAssistantAgent(BaseAgent):
    def __init__(
        self,
        model_client: AzureOpenAIChatCompletionClient,
        session_id: str,
        user_id: str,
        model_context: CosmosBufferedChatCompletionContext,
        verification_assistant_tools: List[Tool],
        verification_assistant_tool_agent_id: AgentId,
    ):
        super().__init__(
            "VerificationAssistantAgent",
            model_client,
            session_id,
            user_id,
            model_context,
            verification_assistant_tools,
            verification_assistant_tool_agent_id,
            "You are an AI Verification Assistant Agent. You specialize in validating, assessing, and verifying various aspects of technology solutions including requirements, architectures, security, performance, compliance, code quality, and documentation. You help ensure that solutions meet standards, work as expected, and align with business objectives."
        ) 