# Earned Value Analysis (EVA) – Interpretation Report

This report presents a detailed analysis and interpretation of Earned Value Analysis (EVA) metrics derived from a multi-module project over a 7-week timeline. The evaluation focuses on schedule performance, cost efficiency, and comparative module outcomes, based entirely on programmatically extracted data from `EVA_Analysis.csv`, in accordance with the assignment requirement to avoid manual calculation.

---

### A. Weeks in Which the Project Was Ahead of Schedule ($SPI > 1$)

To identify periods of faster progress, weeks with a Schedule Performance Index ($SPI > 1$) were examined. An $SPI > 1$ indicates that the Earned Value ($EV$) exceeded the Planned Value ($PV$)—a sign that the project advanced faster than scheduled.

**Key Observations:**

- Several tasks during Weeks 2 through 6 exhibited $SPI > 1$.
- Notably, Module A - Task 2 and Module A - Task 3 recorded $SPI$ values exceeding $2.0$, with a peak $SPI$ of $4.04$ between Weeks 3–5.
- Module B - Task 2 recorded a striking $SPI$ of $10.33$ in Week 7, signaling significant acceleration in schedule adherence.

**Interpretation:** The project outpaced its planned schedule particularly during the mid-to-late phases, with exceptional performance in specific tasks across both modules.

---

### B. Weeks in Which the Project Was Under Budget ($CPI > 1$)

The Cost Performance Index ($CPI$) was used to assess cost efficiency. A $CPI > 1$ indicates that less money was spent than planned for the amount of work completed.

**Key Observations:**

- In Week 3, Module A - Task 2 reported a $CPI$ of $3.64$.
- In Week 7, Module B - Task 2 recorded a $CPI$ of $5.17$.
- $CPI > 1$ was observed in multiple tasks between Weeks 2–6, predominantly within Module A.

**Interpretation:** These figures indicate that select teams delivered work with high cost efficiency during the project’s core execution weeks.

---

### C. Overall Project Status at the End of Week 7

To evaluate the cumulative performance by Week 7, we examined all task-level data corresponding to this week.

**Schedule Status ($SPI$):**

- Values ranged broadly from $0.5$ to $10.33$.
- Module B - Task 2 significantly outperformed expectations with the highest $SPI$.

**Cost Status ($CPI$):**

- Ranged from $0.62$ to $5.17$, indicating variable cost performance.
- Module A - Task 2 and Module B - Task 2 both remained well under budget.

**Cost Variance ($CV$) and Schedule Variance ($SV$):**

- Positive $CV$ and $SV$ were observed in Module A - Task 1 and Task 2, suggesting cost savings and early completion.
- Conversely, Module B - Task 1 displayed negative $CV$ and $SV$, indicating budget overrun and schedule delays.

**Interpretation:** While the project exhibited strong overall performance by Week 7, several tasks—particularly in Module B—require targeted review due to negative variances.

---

### D. Module-Level Performance Comparison (Module A vs. Module B)

A comparative assessment was conducted to evaluate the performance of the two project modules.

**Module A:**

- Demonstrated more consistent $SPI$ and $CPI$ values greater than $1$ across multiple tasks.
- Task 2 stood out for sustained high performance in both cost and schedule metrics.

**Module B:**

- Task 2 showed a strong recovery in Week 7 ($CPI = 5.17$, $SPI = 10.33$).
- Task 1, however, consistently underperformed in both dimensions.

**Interpretation:** Module A demonstrated stronger and more stable execution throughout the project, while Module B exhibited volatility, with a significant rebound limited to Task 2.

---

### E. Analysis of $TCPI$ in Weeks 5 and 6

The To-Complete Performance Index ($TCPI$) was evaluated for Weeks 5 and 6 to understand the level of efficiency required to meet the Budget at Completion ($BAC$) moving forward.

**Key Insights:**

- High $TCPI$ values suggest that exceptionally high future efficiency would be required to remain within budget.
- In Weeks 5 and 6, several tasks exhibited disproportionately high Actual Cost ($AC$) compared to Earned Value ($EV$) growth, implying a widening gap between $EV$ and $BAC$.

**Example:**

- Module B - Task 1 in Week 6 showed $AC$ nearing $BAC$, while $EV$ remained low, resulting in a spike in $TCPI$.

**Interpretation:** These trends indicate that unless significant performance improvements occurred post-Week 6, achieving $BAC$ would likely prove unfeasible for certain tasks.

---

### Conclusion

The EVA analysis reveals that while the project achieved positive overall performance, especially in Module A and certain late-stage tasks in Module B, inconsistencies in cost and schedule efficiency remain. The $TCPI$ trends in Weeks 5 and 6 underscore the importance of timely intervention and performance monitoring to ensure budgetary goals are met.

*All analyses were generated through programmatic methods using `EVA_Analysis.csv`. Manual calculations were intentionally avoided to comply with academic requirements.*
