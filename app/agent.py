"""Prompt agent client: keyless auth, Foundry SDK and Azure Monitor tracing."""

import os

from azure.ai.projects import AIProjectClient
from azure.identity import ClientSecretCredential, DefaultAzureCredential
from azure.monitor.opentelemetry import configure_azure_monitor


def tool_credential() -> ClientSecretCredential:
    """ListAzureResources runs as the app: Azure logs show the app, not the user who asked."""
    return ClientSecretCredential(
        tenant_id=os.environ["AZURE_TENANT_ID"],
        client_id=os.environ["POSTURE_CLIENT_ID"],
        client_secret=os.environ["POSTURE_CLIENT_SECRET"],
    )


def main() -> None:
    configure_azure_monitor()
    client = AIProjectClient(endpoint=os.environ["PROJECT_ENDPOINT"], credential=DefaultAzureCredential())
    openai = client.get_openai_client()
    response = openai.responses.create(
        input="Summarise storage accounts with public network access.",
        extra_body={"agent": {"name": "PostureIQv2", "type": "agent_reference"}},
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
