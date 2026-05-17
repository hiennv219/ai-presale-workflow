## 3. User Flow & Wireframe

### 3.1 User Flow
Developers submit daily reports through a simple web form. The AI engine scans each submission for blockers. If a blocker is detected, it is highlighted on the PM Dashboard for immediate action. Otherwise, the report is logged as a normal status update.

```mermaid
graph TD
    A([Dev opens DailyTools]) --> B[Fills out Daily Report Form]
    B --> C[Submit]
    C --> D[AI Scans Text for Blockers]
    D --> E{Blocker Found?}
    E -- Yes --> F[Highlight on PM Dashboard]
    E -- No --> G[Log as normal status]
    F --> H([PM Reviews Blockers])
```

### 3.2 High-Level Wireframe

**Dev Form**

```
┌─────────────────────────────────────┐
│  📋 Daily Standup                   │
├─────────────────────────────────────┤
│                                     │
│  What I did yesterday:              │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  What I will do today:              │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  Blockers (optional):               │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│           [ Submit ]                │
└─────────────────────────────────────┘
```

**PM Dashboard**

```
┌─────────────────────────────────────┐
│  📊 PM Dashboard                    │
├─────────────────────────────────────┤
│                                     │
│  ⚠️  Active Blockers (2)            │
│  ┌─────────────────────────────┐    │
│  │ • John: API timeout issue   │    │
│  │ • Mai: Waiting for design   │    │
│  └─────────────────────────────┘    │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  📅 Today's Updates                 │
│  ┌─────────────────────────────┐    │
│  │ John - 10:02 AM             │    │
│  │ Did: Fixed auth module      │    │
│  │ Will: Start API integration │    │
│  │ ⚠️ Blocker: API timeout     │    │
│  ├─────────────────────────────┤    │
│  │ Mai - 09:45 AM              │    │
│  │ Did: Completed wireframes   │    │
│  │ Will: Build prototype       │    │
│  │ ⚠️ Blocker: Waiting design  │    │
│  └─────────────────────────────┘    │
│                                     │
└─────────────────────────────────────┘
```
