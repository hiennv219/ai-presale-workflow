## 2. Project Scope

### 2.1 In-Scope
The MVP for DailyTools focuses on the core "Automated PM Bridge" functionality, prioritized by the MoSCoW method:
- **Meeting Capture (Must-have)**: Integration with Zoom and Microsoft Teams via APIs to fetch recordings/transcripts.
- **AI Engine (Must-have)**: Processing of audio/transcripts to generate structured summaries (Executive Summary, Decisions, Action Items).
- **Tool Integration (Must-have)**: Automatic push of results into Jira (as issues or comments) and Notion (as project pages).
- **PM Dashboard (Should-have)**: A lightweight web interface for PMs to configure integrations and review summaries before pushing.

### 2.2 Out-of-Scope
- **Real-time Transcription**: Live text display during the meeting.
- **Standalone Mobile Application**: The initial focus is on the PM's desktop workflow.
- **Google Meet Integration**: Scheduled for Phase 2.
- **Advanced Sentiment Analysis**: Deep psychological insights beyond core task management.

### 2.3 Strategic Assumptions
- **API Availability**: Zoom and Microsoft Teams provide stable API access for recording retrieval.
- **LLM Integration**: Use of advanced LLMs (e.g., GPT-4 or Claude 3) for high-quality summarization.
- **User Permissions**: Clients will grant necessary OAuth permissions for cross-tool integrations.
