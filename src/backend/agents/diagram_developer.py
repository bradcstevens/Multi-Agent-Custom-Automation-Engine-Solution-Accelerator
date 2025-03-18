from typing import List, Dict
import os
import tempfile
import uuid

from autogen_core.base import AgentId
from autogen_core.components import default_subscription
from autogen_core.components.models import AzureOpenAIChatCompletionClient
from autogen_core.components.tools import FunctionTool, Tool

from agents.base_agent import BaseAgent
from context.cosmos_memory import CosmosBufferedChatCompletionContext


# Define Diagram Developer tools (functions)
async def create_system_diagram(
    system_name: str, components: List[str], diagram_type: str
) -> str:
    components_str = ", ".join(components)
    return f"{diagram_type} diagram created for '{system_name}' showing components: {components_str}."


async def design_architecture_diagram(
    project_name: str, architecture_style: str, layers: List[str]
) -> str:
    layers_str = ", ".join(layers)
    return f"Architecture diagram created for '{project_name}' using {architecture_style} style with layers: {layers_str}."


async def create_sequence_diagram(
    interaction_name: str, actors: List[str], steps: int
) -> str:
    actors_str = ", ".join(actors)
    return f"Sequence diagram created for '{interaction_name}' showing interaction between {actors_str} in {steps} steps."


async def design_entity_relationship_diagram(
    database_name: str, entities: List[str], relationship_types: List[str]
) -> str:
    entities_str = ", ".join(entities)
    relationships_str = ", ".join(relationship_types)
    return f"Entity-relationship diagram created for '{database_name}' with entities ({entities_str}) and relationship types: {relationships_str}."


async def create_network_topology_diagram(
    network_name: str, nodes: List[str], connection_types: List[str]
) -> str:
    nodes_str = ", ".join(nodes)
    connections_str = ", ".join(connection_types)
    return f"Network topology diagram created for '{network_name}' with nodes ({nodes_str}) and connection types: {connections_str}."


async def design_process_flow_diagram(
    process_name: str, steps: List[str], decision_points: int
) -> str:
    steps_str = ", ".join(steps)
    return f"Process flow diagram created for '{process_name}' with steps ({steps_str}) and {decision_points} decision points."


async def create_component_diagram(
    system_name: str, components: List[str], interfaces: List[str]
) -> str:
    components_str = ", ".join(components)
    interfaces_str = ", ".join(interfaces)
    return f"Component diagram created for '{system_name}' showing components ({components_str}) and interfaces: {interfaces_str}."


async def design_deployment_diagram(
    system_name: str, environments: List[str], nodes: List[str]
) -> str:
    environments_str = ", ".join(environments)
    nodes_str = ", ".join(nodes)
    return f"Deployment diagram created for '{system_name}' across environments ({environments_str}) with nodes: {nodes_str}."


async def create_class_diagram(
    system_name: str, classes: List[str], relationships: List[str]
) -> str:
    classes_str = ", ".join(classes)
    relationships_str = ", ".join(relationships)
    return f"Class diagram created for '{system_name}' with classes ({classes_str}) and relationships: {relationships_str}."


async def design_state_diagram(
    component_name: str, states: List[str], transitions: int
) -> str:
    states_str = ", ".join(states)
    return f"State diagram created for '{component_name}' with states ({states_str}) and {transitions} transitions."


async def create_use_case_diagram(
    system_name: str, actors: List[str], use_cases: List[str]
) -> str:
    actors_str = ", ".join(actors)
    use_cases_str = ", ".join(use_cases)
    return f"Use case diagram created for '{system_name}' with actors ({actors_str}) and use cases: {use_cases_str}."


async def design_data_flow_diagram(
    system_name: str, processes: List[str], data_stores: List[str], external_entities: List[str]
) -> str:
    processes_str = ", ".join(processes)
    stores_str = ", ".join(data_stores)
    entities_str = ", ".join(external_entities)
    return f"Data flow diagram created for '{system_name}' with processes ({processes_str}), data stores ({stores_str}), and external entities: {entities_str}."


async def create_infrastructure_diagram(
    environment_name: str, servers: List[str], network_components: List[str]
) -> str:
    servers_str = ", ".join(servers)
    components_str = ", ".join(network_components)
    return f"Infrastructure diagram created for '{environment_name}' with servers ({servers_str}) and network components: {components_str}."


async def design_cloud_architecture_diagram(
    cloud_platform: str, services: List[str], regions: List[str]
) -> str:
    services_str = ", ".join(services)
    regions_str = ", ".join(regions)
    return f"Cloud architecture diagram created for {cloud_platform} using services ({services_str}) across regions: {regions_str}."


async def create_container_diagram(
    system_name: str, containers: List[str], interactions: List[str]
) -> str:
    containers_str = ", ".join(containers)
    interactions_str = ", ".join(interactions)
    return f"Container diagram created for '{system_name}' with containers ({containers_str}) and interactions: {interactions_str}."


async def create_azure_architecture_diagram(
    diagram_name: str, 
    components: Dict[str, List[str]],
    relationships: List[Dict[str, str]]
) -> str:
    """
    Create Azure architecture diagram using Python Diagrams library.
    
    Args:
        diagram_name: Name of the diagram
        components: Dictionary mapping Azure service categories to lists of services
                   e.g. {"compute": ["AzureFunction", "AppService"], "database": ["CosmosDB"]}
        relationships: List of dictionaries defining relationships between components
                       e.g. [{"from": "compute.AzureFunction", "to": "database.CosmosDB", "label": "stores data"}]
    
    Returns:
        Path to the generated diagram file
    """
    # Create a unique temporary directory
    temp_dir = tempfile.mkdtemp()
    unique_id = str(uuid.uuid4())[:8]
    file_name = f"{diagram_name.replace(' ', '_')}_{unique_id}"
    diagram_path = os.path.join(temp_dir, f"{file_name}.py")
    
    # Generate Python code for the diagram
    code = [
        "from diagrams import Diagram, Cluster, Edge",
        "from diagrams.azure.compute import *",
        "from diagrams.azure.database import *",
        "from diagrams.azure.storage import *",
        "from diagrams.azure.network import *",
        "from diagrams.azure.analytics import *",
        "from diagrams.azure.integration import *",
        "from diagrams.azure.security import *",
        "from diagrams.azure.web import *",
        "from diagrams.azure.general import *",
        "from diagrams.azure.identity import *",
        "from diagrams.azure.devops import *",
        "from diagrams.azure.ml import *",
        "from diagrams.azure.iot import *",
        "from diagrams.azure.mobile import *",
        "from diagrams.azure.migration import *",
        "from diagrams.azure.management import *",
        "",
        f"with Diagram('{diagram_name}', filename='{file_name}', show=False):",
    ]
    
    # Create component variables
    component_vars = {}
    for category, services in components.items():
        if services:
            code.append(f"    # {category.capitalize()} services")
            for service in services:
                var_name = f"{service.lower().replace('-', '_')}"
                component_vars[f"{category}.{service}"] = var_name
                code.append(f"    {var_name} = {service}('{service}')")
            code.append("")
    
    # Create relationships
    if relationships:
        code.append("    # Relationships")
        for rel in relationships:
            from_var = component_vars.get(rel["from"])
            to_var = component_vars.get(rel["to"])
            if from_var and to_var:
                if "label" in rel:
                    code.append(f"    {from_var} >> Edge(label='{rel['label']}') >> {to_var}")
                else:
                    code.append(f"    {from_var} >> {to_var}")
        code.append("")
    
    # Write the code to a file
    with open(diagram_path, "w") as f:
        f.write("\n".join(code))
    
    # Execute the code to generate the diagram
    try:
        os.system(f"python {diagram_path}")
        output_path = os.path.join(temp_dir, f"{file_name}.png")
        return f"Azure architecture diagram '{diagram_name}' created successfully. The diagram has been saved to {output_path}. The diagram includes components from categories: {', '.join(components.keys())} with {len(relationships)} relationships."
    except Exception as e:
        return f"Failed to create diagram: {str(e)}"


async def create_azure_network_diagram(
    diagram_name: str,
    vnet_config: Dict[str, List[Dict[str, str]]],
    edge_devices: List[str] = None
) -> str:
    """
    Create Azure network topology diagram.
    
    Args:
        diagram_name: Name of the diagram
        vnet_config: Dictionary mapping VNet names to subnet configurations
                    e.g. {"Production VNet": [{"name": "Web Subnet", "cidr": "10.0.1.0/24"}, 
                                             {"name": "Data Subnet", "cidr": "10.0.2.0/24"}]}
        edge_devices: Optional list of edge device names to include
    
    Returns:
        Path to the generated diagram file
    """
    # Create a unique temporary directory
    temp_dir = tempfile.mkdtemp()
    unique_id = str(uuid.uuid4())[:8]
    file_name = f"{diagram_name.replace(' ', '_')}_{unique_id}"
    diagram_path = os.path.join(temp_dir, f"{file_name}.py")
    
    # Generate Python code for the diagram
    code = [
        "from diagrams import Diagram, Cluster, Edge",
        "from diagrams.azure.network import *",
        "from diagrams.azure.compute import VirtualMachine",
        "from diagrams.azure.security import *",
        "from diagrams.azure.general import *",
        "",
        f"with Diagram('{diagram_name}', filename='{file_name}', show=False):"
    ]
    
    # Add a Virtual Network Gateway if we have multiple VNets
    if len(vnet_config) > 1:
        code.append("    vpn_gateway = VirtualNetworkGateway('VPN Gateway')")
        code.append("")
    
    # Create VNets and Subnets
    vnet_vars = {}
    for vnet_name, subnets in vnet_config.items():
        vnet_var = f"vnet_{vnet_name.lower().replace(' ', '_')}"
        vnet_vars[vnet_name] = vnet_var
        code.append(f"    with Cluster('{vnet_name}'):")
        
        # Add Network Security Group
        code.append(f"        nsg_{vnet_var} = NetworkSecurityGroup('NSG')")
        code.append("")
        
        # Add Subnets
        subnet_vars = []
        for subnet in subnets:
            subnet_name = subnet["name"]
            subnet_cidr = subnet["cidr"]
            subnet_var = f"subnet_{subnet_name.lower().replace(' ', '_')}"
            subnet_vars.append(subnet_var)
            code.append(f"        with Cluster('{subnet_name} ({subnet_cidr})'):")
            code.append(f"            {subnet_var} = VirtualNetwork('{subnet_name}')")
            # Add a sample VM in each subnet
            code.append(f"            vm_{subnet_var} = VirtualMachine('VM')")
            code.append(f"            {subnet_var} >> vm_{subnet_var}")
            code.append("")
    
    # Connect VNets if we have multiple
    if len(vnet_config) > 1:
        code.append("    # Connect VNets through Gateway")
        for vnet_name, vnet_var in vnet_vars.items():
            code.append(f"    vpn_gateway >> nsg_{vnet_var}")
        code.append("")
    
    # Add Edge Devices if specified
    if edge_devices:
        code.append("    # Edge Devices")
        code.append("    with Cluster('Edge Devices'):")
        for device in edge_devices:
            device_var = f"device_{device.lower().replace(' ', '_')}"
            code.append(f"        {device_var} = IoTEdge('{device}')")
        code.append("")
        # Connect edge devices to first VNet
        first_vnet = list(vnet_vars.values())[0]
        code.append("    # Connect Edge Devices to Network")
        for device in edge_devices:
            device_var = f"device_{device.lower().replace(' ', '_')}"
            code.append(f"    {device_var} >> nsg_{first_vnet}")
    
    # Write the code to a file
    with open(diagram_path, "w") as f:
        f.write("\n".join(code))
    
    # Execute the code to generate the diagram
    try:
        os.system(f"python {diagram_path}")
        output_path = os.path.join(temp_dir, f"{file_name}.png")
        return f"Azure network diagram '{diagram_name}' created successfully. The diagram has been saved to {output_path}. The diagram includes {len(vnet_config)} VNets with their subnets and security groups."
    except Exception as e:
        return f"Failed to create diagram: {str(e)}"


async def create_azure_serverless_diagram(
    diagram_name: str,
    functions: List[Dict[str, str]],
    storage_services: List[str],
    event_triggers: List[Dict[str, List[str]]]
) -> str:
    """
    Create Azure serverless architecture diagram.
    
    Args:
        diagram_name: Name of the diagram
        functions: List of dictionaries describing Azure Functions
                  e.g. [{"name": "ProcessOrder", "type": "HTTP Trigger"}, {"name": "UpdateInventory", "type": "Queue Trigger"}]
        storage_services: List of Azure storage services to include (e.g., "StorageAccount", "CosmosDB")
        event_triggers: List of event relationships between services
                       e.g. [{"source": "EventHub", "targets": ["ProcessOrder", "UpdateInventory"]}]
    
    Returns:
        Path to the generated diagram file
    """
    # Create a unique temporary directory
    temp_dir = tempfile.mkdtemp()
    unique_id = str(uuid.uuid4())[:8]
    file_name = f"{diagram_name.replace(' ', '_')}_{unique_id}"
    diagram_path = os.path.join(temp_dir, f"{file_name}.py")
    
    # Generate Python code for the diagram
    code = [
        "from diagrams import Diagram, Cluster, Edge",
        "from diagrams.azure.compute import FunctionApp",
        "from diagrams.azure.storage import *",
        "from diagrams.azure.database import *",
        "from diagrams.azure.integration import *",
        "from diagrams.azure.web import AppService",
        "",
        f"with Diagram('{diagram_name}', filename='{file_name}', show=False):"
    ]
    
    # Create function apps with cluster
    code.append("    with Cluster('Function Apps'):")
    function_vars = {}
    for func in functions:
        func_name = func["name"]
        func_type = func["type"]
        func_var = f"func_{func_name.lower().replace(' ', '_')}"
        function_vars[func_name] = func_var
        code.append(f"        {func_var} = FunctionApp('{func_name}\\n({func_type})')")
    code.append("")
    
    # Create storage services
    code.append("    # Storage Services")
    storage_vars = {}
    for service in storage_services:
        service_var = f"{service.lower().replace(' ', '_')}"
        storage_vars[service] = service_var
        code.append(f"    {service_var} = {service}('{service}')")
    code.append("")
    
    # Create event trigger relationships
    code.append("    # Event Relationships")
    for event in event_triggers:
        source = event["source"]
        targets = event["targets"]
        
        # If source is a storage service
        if source in storage_vars:
            source_var = storage_vars[source]
        else:
            # Create the source service if it doesn't exist yet
            source_var = f"{source.lower().replace(' ', '_')}"
            code.append(f"    {source_var} = {source}('{source}')")
            storage_vars[source] = source_var
        
        # Create relationships to target functions
        for target in targets:
            if target in function_vars:
                target_var = function_vars[target]
                code.append(f"    {source_var} >> Edge(label='Trigger') >> {target_var}")
    
    # Add connections from functions to storage
    code.append("")
    code.append("    # Function to Storage Connections")
    for func_name, func_var in function_vars.items():
        for service, service_var in storage_vars.items():
            code.append(f"    {func_var} >> Edge(label='Uses') >> {service_var}")
    
    # Write the code to a file
    with open(diagram_path, "w") as f:
        f.write("\n".join(code))
    
    # Execute the code to generate the diagram
    try:
        os.system(f"python {diagram_path}")
        output_path = os.path.join(temp_dir, f"{file_name}.png")
        return f"Azure serverless architecture diagram '{diagram_name}' created successfully. The diagram has been saved to {output_path}. The diagram includes {len(functions)} function apps and {len(storage_services)} storage services with event relationships."
    except Exception as e:
        return f"Failed to create diagram: {str(e)}"


async def create_azure_microservices_diagram(
    diagram_name: str,
    services: List[Dict[str, str]],
    api_management: bool = True,
    include_loadbalancer: bool = True,
    communication_patterns: List[Dict[str, str]] = None
) -> str:
    """
    Create Azure microservices architecture diagram.
    
    Args:
        diagram_name: Name of the diagram
        services: List of dictionaries describing microservices
                 e.g. [{"name": "UserService", "type": "Container"}, {"name": "OrderService", "type": "App Service"}]
        api_management: Whether to include API Management
        include_loadbalancer: Whether to include a load balancer
        communication_patterns: List of communication patterns between services
                               e.g. [{"from": "UserService", "to": "OrderService", "pattern": "HTTP"}]
    
    Returns:
        Path to the generated diagram file
    """
    # Create a unique temporary directory
    temp_dir = tempfile.mkdtemp()
    unique_id = str(uuid.uuid4())[:8]
    file_name = f"{diagram_name.replace(' ', '_')}_{unique_id}"
    diagram_path = os.path.join(temp_dir, f"{file_name}.py")
    
    # Map service types to appropriate Azure service classes
    service_type_map = {
        "Container": "ContainerInstance",
        "App Service": "AppService",
        "Function": "FunctionApp",
        "AKS": "KubernetesService",
        "VM": "VirtualMachine",
        "Service Fabric": "ServiceFabric",
        "Container App": "ContainerInstance"
    }
    
    # Generate Python code for the diagram
    code = [
        "from diagrams import Diagram, Cluster, Edge",
        "from diagrams.azure.compute import *",
        "from diagrams.azure.web import *",
        "from diagrams.azure.network import *",
        "from diagrams.azure.integration import *",
        "from diagrams.azure.database import *",
        "from diagrams.azure.storage import *",
        "",
        f"with Diagram('{diagram_name}', filename='{file_name}', show=False):"
    ]
    
    # Create clients and frontend
    code.append("    # Clients and Frontend")
    
    if include_loadbalancer:
        code.append("    lb = LoadBalancer('Load Balancer')")
    
    if api_management:
        code.append("    apim = APIManagement('API Management')")
        if include_loadbalancer:
            code.append("    lb >> apim")
    
    code.append("")
    
    # Create service instances
    code.append("    # Microservices")
    service_vars = {}
    for service in services:
        service_name = service["name"]
        service_type = service["type"]
        azure_class = service_type_map.get(service_type, "AppService")  # Default to AppService if type not found
        
        service_var = f"{service_name.lower().replace(' ', '_')}"
        service_vars[service_name] = service_var
        code.append(f"    {service_var} = {azure_class}('{service_name}')")
        
        # Connect services to API Management
        if api_management:
            code.append(f"    apim >> {service_var}")
        elif include_loadbalancer:  # Connect directly to load balancer if no API Management
            code.append(f"    lb >> {service_var}")
    
    code.append("")
    
    # Create communication patterns between services
    if communication_patterns:
        code.append("    # Service Communications")
        for pattern in communication_patterns:
            from_service = pattern["from"]
            to_service = pattern["to"]
            comm_pattern = pattern.get("pattern", "Request")
            
            if from_service in service_vars and to_service in service_vars:
                from_var = service_vars[from_service]
                to_var = service_vars[to_service]
                code.append(f"    {from_var} >> Edge(label='{comm_pattern}') >> {to_var}")
        
        code.append("")
    
    # Add a database layer if needed
    if any("database" in service.get("dependencies", []).lower() for service in services if "dependencies" in service):
        code.append("    # Databases")
        code.append("    cosmos = CosmosDB('Cosmos DB')")
        code.append("    sqldb = SQLDatabase('SQL Database')")
        code.append("")
        
        # Connect services to databases based on dependencies
        for service in services:
            if "dependencies" in service and "database" in service["dependencies"].lower():
                service_var = service_vars[service["name"]]
                if "sql" in service["dependencies"].lower():
                    code.append(f"    {service_var} >> sqldb")
                else:
                    code.append(f"    {service_var} >> cosmos")
    
    # Write the code to a file
    with open(diagram_path, "w") as f:
        f.write("\n".join(code))
    
    # Execute the code to generate the diagram
    try:
        os.system(f"python {diagram_path}")
        output_path = os.path.join(temp_dir, f"{file_name}.png")
        return f"Azure microservices architecture diagram '{diagram_name}' created successfully. The diagram has been saved to {output_path}. The diagram includes {len(services)} microservices with {'API Management, ' if api_management else ''}{'Load Balancer, ' if include_loadbalancer else ''}and communication patterns."
    except Exception as e:
        return f"Failed to create diagram: {str(e)}"


async def create_azure_data_pipeline_diagram(
    diagram_name: str,
    data_sources: List[str],
    processing_services: List[str],
    storage_destinations: List[str],
    flow_steps: List[Dict[str, str]]
) -> str:
    """
    Create Azure data pipeline architecture diagram.
    
    Args:
        diagram_name: Name of the diagram
        data_sources: List of data source services
                     e.g. ["IoTHub", "EventHub", "SQLDatabase"]
        processing_services: List of data processing services
                           e.g. ["DataFactory", "Databricks", "StreamAnalytics"]
        storage_destinations: List of data storage destinations
                            e.g. ["DataLakeStorage", "CosmosDB", "Synapse"]
        flow_steps: List of flow steps between services
                   e.g. [{"from": "IoTHub", "to": "StreamAnalytics", "label": "Stream"}]
    
    Returns:
        Path to the generated diagram file
    """
    # Create a unique temporary directory
    temp_dir = tempfile.mkdtemp()
    unique_id = str(uuid.uuid4())[:8]
    file_name = f"{diagram_name.replace(' ', '_')}_{unique_id}"
    diagram_path = os.path.join(temp_dir, f"{file_name}.py")
    
    # Generate Python code for the diagram
    code = [
        "from diagrams import Diagram, Cluster, Edge",
        "from diagrams.azure.analytics import *",
        "from diagrams.azure.storage import *",
        "from diagrams.azure.database import *",
        "from diagrams.azure.integration import *",
        "from diagrams.azure.iot import *",
        "",
        f"with Diagram('{diagram_name}', filename='{file_name}', show=False):"
    ]
    
    # Create data sources
    code.append("    with Cluster('Data Sources'):")
    source_vars = {}
    for source in data_sources:
        source_var = f"{source.lower().replace(' ', '_')}"
        source_vars[source] = source_var
        code.append(f"        {source_var} = {source}('{source}')")
    code.append("")
    
    # Create processing services
    code.append("    with Cluster('Data Processing'):")
    processing_vars = {}
    for service in processing_services:
        service_var = f"{service.lower().replace(' ', '_')}"
        processing_vars[service] = service_var
        code.append(f"        {service_var} = {service}('{service}')")
    code.append("")
    
    # Create storage destinations
    code.append("    with Cluster('Data Storage'):")
    storage_vars = {}
    for destination in storage_destinations:
        dest_var = f"{destination.lower().replace(' ', '_')}"
        storage_vars[destination] = dest_var
        code.append(f"        {dest_var} = {destination}('{destination}')")
    code.append("")
    
    # Create flow relationships
    code.append("    # Data Flow")
    all_vars = {**source_vars, **processing_vars, **storage_vars}
    
    for flow in flow_steps:
        from_service = flow["from"]
        to_service = flow["to"]
        label = flow.get("label", "Flow")
        
        if from_service in all_vars and to_service in all_vars:
            from_var = all_vars[from_service]
            to_var = all_vars[to_service]
            code.append(f"    {from_var} >> Edge(label='{label}') >> {to_var}")
    
    # Write the code to a file
    with open(diagram_path, "w") as f:
        f.write("\n".join(code))
    
    # Execute the code to generate the diagram
    try:
        os.system(f"python {diagram_path}")
        output_path = os.path.join(temp_dir, f"{file_name}.png")
        return f"Azure data pipeline architecture diagram '{diagram_name}' created successfully. The diagram has been saved to {output_path}. The diagram includes {len(data_sources)} data sources, {len(processing_services)} processing services, and {len(storage_destinations)} storage destinations with detailed data flows."
    except Exception as e:
        return f"Failed to create diagram: {str(e)}"


# Create the DiagramDeveloperTools list
def get_diagram_developer_tools() -> List[Tool]:
    DiagramDeveloperTools: List[Tool] = [
        FunctionTool(
            create_azure_architecture_diagram,
            description="Create an Azure architecture diagram using the Python Diagrams library with Azure components and their relationships.",
            name="create_azure_architecture_diagram",
        ),
        FunctionTool(
            create_azure_network_diagram,
            description="Create an Azure network topology diagram showing VNets, subnets, and networking components.",
            name="create_azure_network_diagram",
        ),
        FunctionTool(
            create_azure_serverless_diagram,
            description="Create an Azure serverless architecture diagram with Function Apps, storage services, and event triggers.",
            name="create_azure_serverless_diagram",
        ),
        FunctionTool(
            create_azure_microservices_diagram,
            description="Create an Azure microservices architecture diagram showing services, API Management, and communication patterns.",
            name="create_azure_microservices_diagram",
        ),
        FunctionTool(
            create_azure_data_pipeline_diagram,
            description="Create an Azure data pipeline architecture diagram showing data sources, processing services, and storage destinations.",
            name="create_azure_data_pipeline_diagram",
        ),
        FunctionTool(
            create_system_diagram,
            description="Create a system diagram showing the components of a system.",
            name="create_system_diagram",
        ),
        FunctionTool(
            design_architecture_diagram,
            description="Design an architecture diagram with specified layers and style.",
            name="design_architecture_diagram",
        ),
        FunctionTool(
            create_sequence_diagram,
            description="Create a sequence diagram showing interactions between actors.",
            name="create_sequence_diagram",
        ),
        FunctionTool(
            design_entity_relationship_diagram,
            description="Design an entity-relationship diagram for a database.",
            name="design_entity_relationship_diagram",
        ),
        FunctionTool(
            create_network_topology_diagram,
            description="Create a network topology diagram showing nodes and connections.",
            name="create_network_topology_diagram",
        ),
        FunctionTool(
            design_process_flow_diagram,
            description="Design a process flow diagram with steps and decision points.",
            name="design_process_flow_diagram",
        ),
        FunctionTool(
            create_component_diagram,
            description="Create a component diagram showing system components and interfaces.",
            name="create_component_diagram",
        ),
        FunctionTool(
            design_deployment_diagram,
            description="Design a deployment diagram showing system deployment across environments.",
            name="design_deployment_diagram",
        ),
        FunctionTool(
            create_class_diagram,
            description="Create a class diagram showing classes and their relationships.",
            name="create_class_diagram",
        ),
        FunctionTool(
            design_state_diagram,
            description="Design a state diagram showing states and transitions for a component.",
            name="design_state_diagram",
        ),
        FunctionTool(
            create_use_case_diagram,
            description="Create a use case diagram showing actors and use cases.",
            name="create_use_case_diagram",
        ),
        FunctionTool(
            design_data_flow_diagram,
            description="Design a data flow diagram showing processes, data stores, and external entities.",
            name="design_data_flow_diagram",
        ),
        FunctionTool(
            create_infrastructure_diagram,
            description="Create an infrastructure diagram showing servers and network components.",
            name="create_infrastructure_diagram",
        ),
        FunctionTool(
            design_cloud_architecture_diagram,
            description="Design a cloud architecture diagram showing services across regions.",
            name="design_cloud_architecture_diagram",
        ),
        FunctionTool(
            create_container_diagram,
            description="Create a container diagram showing containers and their interactions.",
            name="create_container_diagram",
        ),
    ]
    return DiagramDeveloperTools


@default_subscription
class DiagramDeveloperAgent(BaseAgent):
    def __init__(
        self,
        model_client: AzureOpenAIChatCompletionClient,
        session_id: str,
        user_id: str,
        model_context: CosmosBufferedChatCompletionContext,
        diagram_developer_tools: List[Tool],
        diagram_developer_tool_agent_id: AgentId,
    ):
        super().__init__(
            "DiagramDeveloperAgent",
            model_client,
            session_id,
            user_id,
            model_context,
            diagram_developer_tools,
            diagram_developer_tool_agent_id,
            """You are an AI Diagram Developer Agent specialized in creating Azure Solution Architecture diagrams using Python code with the Diagrams library.

You can generate Python code that uses the Diagrams library (https://diagrams.mingrammer.com/) to create clear, professional Azure architecture diagrams with proper Azure icons and components. You leverage the Azure node classes from Diagrams to represent Azure services accurately.

Your specific expertise includes:
1. Creating comprehensive Azure architecture diagrams showing components and their relationships
2. Designing Azure network topology diagrams with VNets, subnets, and connectivity
3. Developing serverless architecture diagrams with Azure Functions and event-driven workflows
4. Building microservices architecture diagrams with appropriate Azure services
5. Designing data pipeline architecture diagrams showing data flow between Azure services

You understand Azure services, their use cases, and proper diagramming conventions for cloud architecture. You create code that generates PNG diagram files that can be shared and presented to stakeholders."""
        ) 