import os
from langchain import OpenAI
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI

# Ensure you have your OpenAI API key set
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Initialize the language model
llm = OpenAI(temperature=0.7)

# Policy Agent
def policy_agent(compliance_document):
    """
    Interprets compliance requirements from a given document.
    """
    prompt = f"""
    You are a compliance expert. Extract the key compliance requirements from the following document and list them as bullet points:

    {compliance_document}
    """
    response = llm(prompt)
    return response.strip()

# Audit Agent
def audit_agent(compliance_requirements, system_configurations):
    """
    Scans system configurations to identify non-compliance.
    """
    prompt = f"""
    You are an audit specialist. Given the compliance requirements and the system configurations, identify areas of non-compliance:

    Compliance Requirements:
    {compliance_requirements}

    System Configurations:
    {system_configurations}

    List any non-compliant items with explanations.
    """
    response = llm(prompt)
    return response.strip()

# Reporting Agent
def reporting_agent(audit_findings):
    """
    Generates a report with actionable insights based on audit findings.
    """
    prompt = f"""
    You are a reporting analyst. Based on the following audit findings, generate a report with actionable insights:

    Audit Findings:
    {audit_findings}

    The report should include:
    - A summary of findings
    - Detailed explanations
    - Recommended actions
    """
    response = llm(prompt)
    return response.strip()

# Sample Data
compliance_document = """
All user passwords must be at least 12 characters long and include a mix of uppercase letters, lowercase letters, numbers, and special characters. 
User accounts must be locked after 5 failed login attempts. 
Sensitive data at rest and in transit must be encrypted using industry-standard encryption algorithms.
"""

system_configurations = """
- User passwords are set to a minimum of 8 characters, requiring letters and numbers.
- User accounts are locked after 10 failed login attempts.
- Sensitive data at rest is encrypted using AES-256.
- Data in transit is transmitted without encryption.
"""

# Orchestrating the Workflow
def main():
    # Step 1: Policy Agent interprets compliance requirements
    print("Running Policy Agent...")
    compliance_requirements = policy_agent(compliance_document)
    print("\nCompliance Requirements:\n")
    print(compliance_requirements)
    print("\n" + "="*80 + "\n")

    # Step 2: Audit Agent scans system configurations for non-compliance
    print("Running Audit Agent...")
    audit_findings = audit_agent(compliance_requirements, system_configurations)
    print("\nAudit Findings:\n")
    print(audit_findings)
    print("\n" + "="*80 + "\n")

    # Step 3: Reporting Agent generates a report with actionable insights
    print("Running Reporting Agent...")
    report = reporting_agent(audit_findings)
    print("\nGenerated Report:\n")
    print(report)

if __name__ == "__main__":
    main()
