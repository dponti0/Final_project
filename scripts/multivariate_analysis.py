"""
Script for carrying out the multivariate visual analysis
"""

# Import the required libraries
import matplotlib.pyplot as plt
import seaborn as sns


class MultivariateVisualizer:
    """
    Class that includes all the functions of the multivariate analysis
    """

    def __init__(self, df, pdf_pages=None):
        self.df = df
        self.pdf_pages = pdf_pages

    def save_and_close(self):
        """
        Function to handle the saving and closing of the figures
        """

        if self.pdf_pages:
            self.pdf_pages.savefig()
        plt.close()

    def age_stroke_distribution(self):
        """
        Function to conduct the age-stroke relation study
        """
        _, ax = plt.subplots(figsize=(12, 6))

        # Bar plot for age category distribution
        sns.countplot(x="age_cat", hue="stroke", data=self.df, palette="pastel", ax=ax)
        ax.set_title("Age Category-Stroke Distribution", fontweight="bold")
        ax.set_xlabel("Age Category", fontstyle="italic")
        ax.set_ylabel("Count", fontstyle="italic")

        # Intermittent background lines on the horizontal axis
        ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

        # Legend & decoration
        ax.legend(title="Stroke", loc="upper right", labels=["No", "Yes"])

        sns.despine(trim=True, left=True)

        # Save & close the function
        self.save_and_close()

    def glucose_stroke_distribution(self):
        """
        Function to conduct the glucose-stroke relation study (kdeplot)
        """

        _, ax = plt.subplots(figsize=(12, 6))

        # KDE plot
        sns.kdeplot(
            data=self.df,
            x="avg_glucose_level",
            hue="stroke",
            fill=True,
            common_norm=False,
            palette="viridis",
            ax=ax,
        )
        ax.set_title(
            "Distribution of Average Glucose Level by Stroke", fontweight="bold"
        )
        ax.set_xlabel("Average Glucose Level", fontstyle="italic")
        ax.set_ylabel("Density", fontstyle="italic")

        # Intermittent background lines on the horizontal axis
        ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

        # Appearance of the frames & legend
        sns.despine(trim=True, left=True, ax=ax)

        ax.legend(labels=["Stroke", "Non Stroke"], fontsize="8")

        # Save and close the function
        self.save_and_close()

    def bmi_stroke_distribution(self):
        """
        Function to create the violinplot and conduct the bmi-stroke study
        """

        _, ax = plt.subplots(figsize=(12, 6))

        # Violin plot for BMI-Stroke distribution
        sns.violinplot(x="stroke", y="bmi", data=self.df, palette="Set2", ax=ax)

        # Title and axis labels
        ax.set_title("Distribution of BMI by Stroke", fontweight="bold", fontsize=14)
        ax.set_xlabel("Stroke (0: No, 1: Yes)", fontstyle="italic", fontsize=10)
        ax.set_ylabel("BMI", fontstyle="italic", fontsize=10)

        # Intermittent background lines on the horizontal axis
        ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

        # Appearance of the frames
        sns.despine(trim=True, left=True, ax=ax)

        self.save_and_close()

    def bmi_glucose_scatter(self):
        """
        Function to create the scatterplot and conduct the bmi-glucose study
        """
        plt.figure(figsize=(12, 8))

        # Scatter plot for 'No' (stroke=0)
        sns.scatterplot(
            x="bmi",
            y="avg_glucose_level",
            data=self.df[self.df["stroke"] == 0],
            color="#1f77b4",
            alpha=0.5,
            label="No Stroke",
        )

        # Scatter plot for 'Yes' (stroke=1)
        sns.scatterplot(
            x="bmi",
            y="avg_glucose_level",
            data=self.df[self.df["stroke"] == 1],
            color="#ff7f0e",
            alpha=1,
            label="Stroke",
        )

        # Title, labels & legend
        plt.title("BMI-Glucose Scatter Plot with Stroke", fontweight="bold")
        plt.xlabel("BMI", fontstyle="italic")
        plt.ylabel("Average Glucose Level", fontstyle="italic")
        plt.legend()

        self.save_and_close()

    def heart_disease_gender_age(self):
        """
        Visualize the heart disease-gender distribution
        """
        plt.figure(figsize=(12, 6))

        sns.barplot(
            x="age_group",
            y="heart_disease",
            hue="gender",
            data=self.df,
            palette="pastel",
        )

        plt.title("Heart Disease per Gender and Age Range", fontweight="bold")
        plt.xlabel("Age Range", fontstyle="italic")
        plt.ylabel("Heart Disease (0: No, 1: Yes)", fontstyle="italic")
        plt.legend()

        self.save_and_close()

    def glucose_smoking_distribution(self):
        """
        Function for creating a stripplot and conducting the glucose-smoking study
        """

        plt.figure(figsize=(12, 6))

        # Style
        colors = {0: "#7FB3D5", 1: "#E88E5A"}
        labels = {0: "Non-Heart Disease", 1: "Heart Disease"}

        # Strip plot figure
        sns.stripplot(
            x="smoking_status",
            y="avg_glucose_level",
            hue="heart_disease",
            data=self.df,
            palette=colors,
            dodge=True,
            jitter=0.2,
            size=8,
        )

        plt.title(
            "Glucose Levels between Smokers and Non-smokers",
            fontweight="bold",
            fontsize=12,
        )
        plt.xlabel("Smoking Status", fontstyle="italic", fontsize=10)
        plt.ylabel("Average Glucose Level", fontstyle="italic", fontsize=10)

        # Legend with labels and adjusted size
        legend_labels = [
            plt.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                label=labels[i],
                markerfacecolor=colors[i],
                markersize=8,
            )
            for i in labels
        ]

        plt.legend(
            handles=legend_labels, loc="upper right", bbox_to_anchor=(1, 1), fontsize=6
        )

        # Intermittent horizontal line & glucose threshold message
        threshold_glucose = 140
        plt.axhline(y=threshold_glucose, color="gray", linestyle="--", linewidth=0.5)
        plt.text(
            3,
            threshold_glucose + 2,
            "Threshold Glucose Level",
            fontstyle="italic",
            color="black",
            fontsize=6,
        )

        self.save_and_close()

    def age_bmi_relation(self):
        """
        Function to create the Kdeplot (age-bmi relation study)
        """

        plt.figure(figsize=(12, 6))

        # Kdeplot with colors and transparency
        sns.kdeplot(
            x="age",
            y="bmi",
            data=self.df,
            fill=True,
            cmap="coolwarm",
            levels=5,
            thresh=0.05,
        )

        # Intermittent gray lines on the horizontal axis
        plt.axhline(y=20, color="gray", linestyle="--", linewidth=0.8)
        plt.axhline(y=25, color="gray", linestyle="--", linewidth=0.8)
        plt.axhline(y=30, color="gray", linestyle="--", linewidth=0.8)

        plt.title("Age-BMI Relation", fontweight="bold", fontsize=12, loc="center")
        plt.xlabel("Age", fontstyle="italic", fontsize=11)
        plt.ylabel("BMI", fontstyle="italic", fontsize=11)

        # Descriptive labels
        plt.text(80, 18, "Underweight", color="black", fontsize=8, fontstyle="italic")
        plt.text(80, 23, "Normal Weight", color="black", fontsize=8, fontstyle="italic")
        plt.text(80, 28, "Overweight", color="black", fontsize=8, fontstyle="italic")

        # Save & close
        self.save_and_close()

    def work_type_stroke_distribution(self):
        """
        Function to create a countplot for the work type-strokes relation
        """
        plt.figure(figsize=(11, 6))

        # Style
        colors = ["#ADD8E6", "#FFD700"]
        ax = sns.countplot(x="work_type", hue="stroke", data=self.df, palette=colors)

        # Title and axis labels
        ax.set_title("Work Type - Stroke Distribution", fontsize=14, fontweight="bold")
        ax.set_xlabel("Work Type", fontstyle="italic", fontsize=10)
        ax.set_ylabel("Number of People", fontstyle="italic", fontsize=10)

        # Legend
        ax.legend(fontsize="10", labels=["Non Stroke", "Stroke"])

        # Axis and background style
        sns.despine(trim=True, left=True)

        # Intermittent background lines on the horizontal axis
        ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

        self.save_and_close()

    def marriage_glucose_relation(self):
        """
        Function to create the Kdeplot (marriage-glucose study)
        """
        plt.figure(figsize=(12, 6))

        # KDE plot
        sns.kdeplot(
            data=self.df,
            x="avg_glucose_level",
            hue="ever_married",
            fill=True,
            common_norm=False,
            palette="pastel",
        )

        # Title & labels
        plt.title(
            "Marriage - Average Glucose Level Relation", fontweight="bold", fontsize=14
        )
        plt.xlabel("Average Glucose Level", fontstyle="italic", fontsize=10)
        plt.ylabel("Density", fontstyle="italic", fontsize=10)

        # Background lines
        plt.gca().yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

        # Appearance
        sns.despine(trim=True, left=True)

        # Legend with labels and size
        labels = {0: "Married", 1: "Not married"}
        legend_labels = [
            plt.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                label=labels[i],
                markerfacecolor=sns.color_palette("pastel")[i],
                markersize=8,
            )
            for i in labels
        ]

        plt.legend(
            handles=legend_labels, loc="upper right", bbox_to_anchor=(1, 1), fontsize=10
        )

        # Save & close
        self.save_and_close()

    def age_stroke_rate_lineplot(self):
        """
        Function to create the age-stroke lineplot
        """

        # Style
        sns.set(style="whitegrid")

        # Figure and axes
        _, ax = plt.subplots(figsize=(12, 6))

        # Calculate the stroke rate per age group
        age_groups = self.df["age_cat"].unique()
        stroke_rate = []
        for age_group in age_groups:
            subset = self.df[self.df["age_cat"] == age_group]
            stroke_rate.append(subset["stroke"].mean())

        # Reverse the order of age groups
        age_groups = age_groups[::-1]
        stroke_rate = stroke_rate[::-1]

        # Create the line plot
        sns.lineplot(x=age_groups, y=stroke_rate, color="#0f4c81", ax=ax, marker="o")

        # Background lines on the horizontal axis
        ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

        # Appearance of the frames
        sns.despine(trim=True, left=True)

        # Labels to the chart
        ax.set_title("Stroke Rate by Age Group", fontweight="bold", fontsize=14)
        ax.set_xlabel("Age Group", fontstyle="italic", fontsize=10)
        ax.set_ylabel("Stroke Rate", fontstyle="italic", fontsize=10)

        # Save and close the chart in the PDF
        self.save_and_close()

    def marriage_bmi_relation(self):
        """
        Function to generate the marriage-bmi graph
        """
        # Set the style of Seaborn charts
        sns.set(style="whitegrid")

        # Set the background color
        background_color = "#f6f5f5"

        # Create the figure and axes
        _, ax = plt.subplots(figsize=(12, 6), facecolor=background_color)
        ax.set_facecolor(background_color)

        # Create the kernel density estimate (kdeplot)
        sns.kdeplot(
            data=self.df,
            x="bmi",
            hue="ever_married",
            fill=True,
            common_norm=False,
            palette="Set2",
            ax=ax,
        )

        # Add intermittent background lines on the horizontal axis
        ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

        # Customize the appearance of the frames
        sns.despine(trim=True, left=True)

        # Add legend with labels and adjust size
        labels = {0: "Married", 1: "Not Married"}
        legend_labels = [
            plt.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                label=labels[i],
                markerfacecolor=sns.color_palette("Set2")[i],
                markersize=8,
            )
            for i in labels
        ]

        plt.legend(
            handles=legend_labels, loc="upper right", bbox_to_anchor=(1, 1), fontsize=10
        )

        # Add labels to the chart
        ax.set_title("Marriage - BMI Relation", fontweight="bold", fontsize=14)
        ax.set_xlabel("BMI", fontstyle="italic", fontsize=10)
        ax.set_ylabel("Density", fontstyle="italic", fontsize=10)

        # Save and close the chart
        self.save_and_close()

    def correlation_heatmap(self):
        """
        Function to generate the correlation heatmap
        """

        # Select the numerical columns
        numeric_columns = self.df.select_dtypes(include=["number"]).columns
        numeric_df = self.df[numeric_columns]

        # Style
        sns.set(style="white")

        # Calculate the correlation matrix
        correlation_matrix = numeric_df.corr()

        # Figure and axis
        _, ax = plt.subplots(figsize=(12, 9))

        # Create the heatmap
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap="Blues",
            fmt=".2f",
            linewidths=0.35,
            ax=ax,
        )

        # Labels & titles
        ax.set_title("Correlation Heatmap", fontweight="bold", fontsize=16)
        ax.set_xticklabels(
            ax.get_xticklabels(), rotation=45, horizontalalignment="right", fontsize=7.5
        )
        ax.set_yticklabels(ax.get_yticklabels(), fontsize=7)
        ax.set_title("Correlation Heatmap", fontweight="bold", fontsize=14)

        # Save in the PDF
        self.save_and_close()

    def overall_health_pie_chart(self):
        """
        Function to generate a pie chart about the overall health
        """

        health_counts = self.df["overall_health"].value_counts()

        # Colors
        colors = ["#1f78b4", "#5593c8", "#74a7d2", "#caddee", "#abcae4"]

        # Emphasize the 'Very Good' slice
        explode = [0, 0, 0.1, 0, 0]

        # Two subplots, one for the pie chart and one for the label
        _, _ = plt.subplots(figsize=(8, 8))
        ax_pie = plt.subplot(111)

        # Create the pie chart
        ax_pie.pie(
            health_counts,
            labels=health_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            explode=explode,
            shadow=True,
            textprops={"fontstyle": "italic"},
            wedgeprops={"edgecolor": "black", "linewidth": 1.5, "width": 0.2},
        )

        # Title
        ax_pie.set_title("Distribution of Overall Health", fontweight="bold", size=14)

        # Save in the PDF
        self.save_and_close()
