import pandas as pd
import matplotlib.pyplot as plt

def dashboard(marks_csv):
    df=pd.read_csv(marks_csv)
    df.fillna(0,inplace=True)

    # Subject-wise average
    subject_avgs=df.drop(columns=["enrollment","name"]).mean()
    subject_avgs.to_csv("summary.csv")

    # Grade distribution
    df["Total"]=df.drop(columns=["enrollment","name"]).sum(axis=1)
    plt.hist(df["Total"],bins=5,color="skyblue")
    plt.title("Grade Distribution")
    plt.savefig("grade_distribution.png"); plt.close()

    # Subject average comparison
    subject_avgs.plot(kind="bar",color="orange")
    plt.title("Subject Averages")
    plt.savefig("subject_average.png"); plt.close()

    # Top performers
    top=df.nlargest(3,"Total")
    plt.bar(top["name"],top["Total"],color="green")
    plt.title("Top Performers")
    plt.savefig("top_performers.png"); plt.close()

    print("Dashboard exported")

# ---------------- SAMPLE INPUT ----------------
# marks.csv:
# enrollment,name,Python,DBMS,OS
# 101,Riya,85,90,80
# 102,Karan,70,75,65
# 103,Meera,95,88,92
# 104,Dev,60,55,70

dashboard("marks.csv")
