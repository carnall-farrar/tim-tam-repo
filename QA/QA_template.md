# QA Process

This document provides a template for the checks required for QA.

For hybrid projects where the main branch is not 'production', we assume code has been merged onto main before being QAed (following code review during the PR). For each task being QA'ed:

1. Create a QA branch from main
2. Copy the template below into a new file and complete checks
3. Open a PR with your completed file and merge onto main
4. Delete the QA branch

In the future QA should occur before the code is merged to main, but let's walk before we can run.

### _Template begins here_:

---

## <Short title for task>

**QAer:**  
**Developer:**  
**QA date:**  
**Task ID:**

---

### Code

**QA's description of task:**  
**Is the code readable?** Not at all / Sometimes / *Mostly / *Completely  
**Does the code follow best practices?** Not at all / Sometimes / *Mostly / *Completely  
**Can you run the code?** *Yes / No  
**Can you produce the same output as the developer?** *Yes / No  
**Comparison to manual calculations (if feasible):**  
**Any feedback for developer on code:**

\*Required for acceptance

---

### Approach

**Comparison to external data / sense check of outputs:**  
**Is the approach fit for purpose?** *Yes / No (with justification)  
**What are the risks of the approach and are they acceptable?** *Yes / No with risks described  
**Any feedback for developer on approach:**

\*Required for acceptance

---

### Summary and approval

**Scope of approval:**  
**Summary:**  
**Approval given:** ✅ / ❌
