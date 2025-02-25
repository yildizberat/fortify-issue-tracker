import requests
import pandas as pd
import matplotlib.pyplot as plt

# API Configuration
BASE_URL = "https://your-fortify-instance.com/ssc/api/v1"
API_TOKEN = "YOUR_API_TOKEN_HERE"
HEADERS = {
    "Authorization": f"FortifyToken {API_TOKEN}",
    "Accept": "application/json"
}

def get_projects():
    """Fetch all projects from Fortify SSC."""
    response = requests.get(f"{BASE_URL}/projects?fields=id,name&limit=200", headers=HEADERS)
    return response.json().get("data", [])

def get_project_versions(project_id):
    """Fetch versions for a given project."""
    response = requests.get(f"{BASE_URL}/projects/{project_id}/versions", headers=HEADERS)
    return response.json().get("data", [])

def get_issues(version_id, project_name):
    """Fetch issues for a specific project version."""
    start = 0
    limit = 500
    all_issues = []

    while True:
        response = requests.get(
            f"{BASE_URL}/projectVersions/{version_id}/issues?fields=id,issueName,severity&start={start}&limit={limit}",
            headers=HEADERS
        )
        data = response.json()
        issues = data.get("data", [])
        
        if not issues:
            break
        
        for i in issues:
            severity = i.get("severity", 0.0) or 0.0

            # Determine Risk Level
            if severity >= 4.0:
                risk_level = "Critical"
            elif severity >= 2.5:
                risk_level = "High"
            elif severity < 2.5 and severity > 0:
                risk_level = "Medium"
            else:
                risk_level = "Low"

            all_issues.append({
                "Project Name": project_name,
                "Issue ID": i["id"],
                "Issue Name": i["issueName"],
                "Severity": severity,
                "Risk Level": risk_level
            })

        start += limit

    return all_issues

def main():
    all_issues = []
    projects = get_projects()
    
    for project in projects:
        project_id = project["id"]
        project_name = project["name"]
        
        versions = get_project_versions(project_id)
        for version in versions:
            version_id = version["id"]
            issues = get_issues(version_id, project_name)
            all_issues.extend(issues)
    
    df = pd.DataFrame(all_issues)
    df.to_csv("fortify_issues.csv", index=False)
    print("Issue report saved: fortify_issues.csv")

    # Generate visualization
    if not df.empty:
        risk_counts = df["Risk Level"].value_counts()
        plt.figure(figsize=(8, 6))
        risk_counts.plot(kind="bar", color=["red", "orange", "yellow", "green"])
        plt.xlabel("Risk Level")
        plt.ylabel("Issue Count")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

if __name__ == "__main__":
    main()
