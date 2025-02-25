# Fortify Issue Tracker

## 📌 Description
Fortify Issue Tracker is a Python-based tool that fetches and analyzes security vulnerabilities from the Fortify Software Security Center (SSC) API. It categorizes vulnerabilities based on severity levels (Critical, High, Medium) and generates detailed reports, including visual representations of risk levels.

## 🚀 Features
- **Fetches security vulnerabilities** from Fortify SSC API
- **Categorizes vulnerabilities** based on severity scores
- **Generates CSV reports** for easy analysis
- **Creates visualizations** to represent security risks
- **Supports automated batch processing** for multiple projects

## 🛠️ Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/fortify-issue-tracker.git
   cd fortify-issue-tracker
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🏃 Usage
Run the script to fetch security issues and generate reports:
```sh
python report.py
```

### Example Output:
- `fortify_issues.csv`: A detailed report of vulnerabilities
- **Visual Graphs**: A bar chart showing vulnerabilities categorized by severity

## 📊 Visualization
The script generates graphs showing:
- The **top 5 most common vulnerabilities** for each risk level (Critical, High, Medium)
- A **distribution chart** of vulnerabilities across different severity levels

### Risk Matrix
![Risk Matrix](8B44717C-75C5-487E-BA3F-ADD5FF5A7F52.png)

## 🔧 Configuration
To modify API settings, update the `BASE_URL` and `TOKEN` in `report.py`.



---

Contributions are welcome! Feel free to open issues and submit pull requests. 🚀
