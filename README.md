# AI Presale Workspace

Welcome to the AI Presale Workspace! 👋 

This tool helps you quickly turn messy customer notes into polished Proposals and Work Breakdown Structures (WBS). Everything happens right inside your AI chat. 

No complex setup, no software to install. Just tell the AI what you need using simple commands, and it handles the rest!

## 🚀 Quick Start Guide

You drive the workflow using **slash commands** in your AI chat. Here is the typical flow from start to finish:

### 1. Start a New Project
```text
/presale-init project: Acme App
```
This creates a fresh workspace folder for your new deal.

### 2. Build the Proposal
```text
/presale-run

Client: Acme Corp
Requirements:
- Build an order management system
- Integrate online payments
- Mobile app for end-users
```
Paste your meeting notes, raw requirements, or emails here. The AI will guide you through the process, ask clarifying questions if needed, and generate a structured Draft Proposal and WBS.

### 3. Update with Feedback
```text
/presale-update

Client feedback:
- The budget is capped at $200K.
- We need this done in 6 months.
```
When the client asks for changes, use this command. The AI smartly updates only the affected sections of your documents, keeping everything in sync.

### 4. Finalize & Export
Once you are happy with the drafts, run:
```text
/presale-finalize
```
The AI runs a final consistency check to ensure the Proposal and WBS match perfectly.

Then, export the final documents for the client:
```text
/presale-export
```
Your ready-to-send HTML/PDF files will appear in your project's `_delivery/` folder.

## 📁 Where is Everything?

- **`projects/`**: Your active deals. Each project gets a neat folder containing your raw inputs (`_source/`), working drafts (`workspace/`), and final exports (`_delivery/`).
- **`.agent/`**: The system's brain. It holds all the rules, workflows, and templates the AI uses to do its job.

## 🧠 Key Things to Know

- **We don't guess:** If critical information is missing, the AI stops and asks you. It will never invent facts.
- **No silent scope creep:** If a new requirement pops up, the AI will flag it so you can approve it first.
- **Perfect sync:** Your Proposal and WBS will always match. The AI won't let you finalize if they are out of alignment.

Happy presaling! 🎉
