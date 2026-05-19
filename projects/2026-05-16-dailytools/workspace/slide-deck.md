---
marp: true
theme: default
paginate: true
header: "DailyTools MVP"
footer: "Antigravity AI — Confidential"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;700;900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;700&display=swap');

  section {
    font-family: 'Inter', 'Noto Sans SC', sans-serif;
    background-color: #fafaf8;
    color: #0a0a0a;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    border-radius: 0 !important;
    border: 1px solid #0a0a0a;
    box-sizing: border-box;
  }

  section.cover {
    background-color: #002FA7;
    color: #fafaf8;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 80px;
  }

  section.cover h1 {
    font-family: 'Inter Tight', sans-serif;
    font-size: 72px;
    font-weight: 900;
    color: #fafaf8;
    border: none;
    margin: 0;
    text-transform: uppercase;
    line-height: 1.1;
    text-align: left;
  }

  section.cover .meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    display: flex;
    justify-content: space-between;
    border-top: 1px solid rgba(250, 250, 248, 0.3);
    padding-top: 20px;
    color: #fafaf8;
  }

  h1 {
    font-family: 'Inter Tight', sans-serif;
    font-size: 40px;
    font-weight: 700;
    color: #002FA7;
    border-bottom: 2px solid #002FA7;
    padding-bottom: 10px;
    margin-top: 0;
    margin-bottom: 30px;
    text-transform: uppercase;
  }

  h2 {
    font-family: 'Inter Tight', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #002FA7;
    margin-top: 0;
    margin-bottom: 20px;
    text-transform: uppercase;
  }

  h3 {
    font-family: 'Inter Tight', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #0a0a0a;
    margin: 0 0 10px 0;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  p {
    font-size: 16px;
    line-height: 1.5;
    margin-top: 0;
    margin-bottom: 15px;
  }

  .columns {
    display: flex;
    gap: 30px;
    width: 100%;
  }

  .column {
    flex: 1;
  }

  .card {
    background-color: #f5f5f2;
    border: 1px solid #0a0a0a;
    border-radius: 0;
    padding: 20px;
    margin-bottom: 15px;
    box-sizing: border-box;
  }

  .card.accent {
    border-color: #002FA7;
    border-width: 2px;
    background-color: rgba(0, 47, 167, 0.03);
  }

  .highlight {
    color: #002FA7;
    font-weight: 700;
  }

  blockquote {
    border-left: 4px solid #002FA7;
    padding-left: 20px;
    margin: 20px 0;
    font-style: italic;
    color: #444;
    font-size: 18px;
  }

  .vertical-timeline {
    position: relative;
    padding-left: 30px;
    border-left: 1px dashed #0a0a0a;
  }

  .timeline-node {
    position: relative;
    margin-bottom: 25px;
  }

  .timeline-node::before {
    content: '';
    position: absolute;
    left: -36px;
    top: 5px;
    width: 10px;
    height: 10px;
    background-color: #002FA7;
    border: 1px solid #0a0a0a;
  }

  .badge-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #002FA7;
    margin-bottom: 10px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
  }

  th {
    background-color: #002FA7;
    color: #fafaf8;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    text-align: left;
    padding: 10px 15px;
    border: 1px solid #0a0a0a;
    text-transform: uppercase;
  }

  td {
    padding: 10px 15px;
    border: 1px solid #0a0a0a;
    font-size: 15px;
    background-color: #fafaf8;
  }

  pre {
    background-color: #fafaf8;
    border: 1px solid #0a0a0a;
    border-radius: 0;
    padding: 15px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    overflow: auto;
    margin: 0;
  }
---

<!-- _class: cover -->

<div class="dots" style="font-family: 'JetBrains Mono', monospace; opacity: 0.3; line-height: 1.2; letter-spacing: 0.5em; font-size: 18px; margin-bottom: 10px; color: #fafaf8;">
• • • • • • • •<br>
• • • • • • • •<br>
• • • • • • • •
</div>

# DAILYTOOLS MVP

<div class="meta">
  <span>No. 01 / PROPOSAL</span>
  <span>AUTOMATED BLOCKER DETECTION</span>
  <span>May 2026</span>
</div>

---

# The Problem

<div class="badge-number">No. 02 / ANALYSIS</div>

<div class="columns">
<div class="column card">
  <h3>01 / LACK OF VISIBILITY</h3>
  <p>Daily developer reports are too long, unstructured, and buried deep inside chat channel histories.</p>
</div>
<div class="column card">
  <h3>02 / MANUAL PARSING</h3>
  <p>Project Managers spend <strong>30–60 minutes per day</strong> manually reading Slack just to extract issues.</p>
</div>
</div>

<blockquote>
  "If a blocker is missed for 1 day, it can become a 1-week delay."
</blockquote>

---

# Our Solution

<div class="badge-number">No. 03 / PRODUCT</div>

<div class="columns">
<div class="column" style="flex: 0.7;">
  <p style="font-size: 20px; line-height: 1.6; color: #002FA7; font-weight: 500;">
    A lightweight, frictionless web application that automatically collects developer daily updates and leverages AI to instantly surface hidden blockers.
  </p>
</div>
<div class="column" style="flex: 1.3;">
  <div class="card">
    <h3>01 / FRICTIONLESS DAILY LOG</h3>
    <p>A simple 3-field form that developers can fill out in under 30 seconds.</p>
  </div>
  <div class="card">
    <h3>02 / SMART BLOCKER DETECTION</h3>
    <p>AI scans submissions, reading between the lines to flag risks instantly.</p>
  </div>
  <div class="card accent">
    <h3>03 / ALERT DASHBOARD</h3>
    <p>PMs see all flagged blockers on a single screen without manual parsing.</p>
  </div>
</div>
</div>

---

# How It Works

<div class="badge-number">No. 04 / PROCESS</div>

<div style="display: flex; justify-content: space-between; border-top: 1px dashed #0a0a0a; margin-top: 40px; padding-top: 30px;">
  <div style="flex: 1; margin-right: 15px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">STEP 01</div>
    <h3 style="margin-top: 5px;">Dev Form</h3>
    <p style="font-size: 15px; color: #555;">Developer opens DailyTools and fills out the 30-second daily form.</p>
  </div>
  <div style="flex: 1; margin-right: 15px; border-left: 1px solid #002FA7; padding-left: 15px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">STEP 02</div>
    <h3 style="margin-top: 5px;">AI Scanning</h3>
    <p style="font-size: 15px; color: #555;">The AI scans the text to extract blockers and analyze risks.</p>
  </div>
  <div style="flex: 1; border-left: 1px solid #002FA7; padding-left: 15px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">STEP 03</div>
    <h3 style="margin-top: 5px;">Alert Dashboard</h3>
    <p style="font-size: 15px; color: #555;">Blockers trigger alerts on the PM Dashboard instantly.</p>
  </div>
</div>

---

# System Architecture

<div class="badge-number">No. 05 / TECHNICAL</div>

<div class="columns">
<div class="column" style="flex: 1.2;">
  <pre style="font-size: 12px; line-height: 1.35;">
┌─ CLIENT (Next.js) ───────────┐
│  Dev Form  │  PM Dashboard   │
└──────────────┬───────────────┘
               │ (HTTPS REST)
               ▼
┌─ API GATEWAY ────────────────┐
│  Auth  │ Submit │ Blockers   │
└──────────────┬───────────────┘
               │ (JSON Payload)
               ▼
┌─ AI ENGINE (GPT-4o) ─────────┐
│  Text scanner & risk model   │
└──────────────┬───────────────┘
               │ (Store/Query)
               ▼
┌─ DB (Supabase / Postgres) ───┐
│  reports │ blockers │ users  │
└──────────────────────────────┘
  </pre>
</div>
<div class="column" style="flex: 0.8; display: flex; flex-direction: column; justify-content: space-between;">
  <div class="card" style="margin: 0; height: 100%;">
    <h3>Architecture Spec</h3>
    <ul style="font-size: 14px; padding-left: 20px; line-height: 1.5; margin: 0; color: #333;">
      <li><strong>Monolithic Speed</strong>: Next.js unified build for extremely fast MVP rollout.</li>
      <li><strong>Cognitive Layer</strong>: OpenAI GPT-4o API for deep contextual text parsing.</li>
      <li><strong>Serverless DB</strong>: Supabase Postgres ensures instant state synchronization.</li>
    </ul>
  </div>
</div>
</div>

---

# Tech Stack

<div class="badge-number">No. 06 / SPECIFICATION</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; width: 100%;">
  <div class="card" style="margin: 0;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #002FA7;">01 / FRONTEND & BACKEND</div>
    <h3 style="margin-top: 5px;">Next.js & TypeScript</h3>
    <p style="font-size: 14px; margin: 0; color: #555;">Single-repo stack for rapid development, strict type safety, and fast routing.</p>
  </div>
  <div class="card" style="margin: 0;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #002FA7;">02 / AI ENGINE</div>
    <h3 style="margin-top: 5px;">OpenAI GPT-4o</h3>
    <p style="font-size: 14px; margin: 0; color: #555;">Advanced reasoning model to detect implicit, non-obvious dev blocker signals.</p>
  </div>
  <div class="card" style="margin: 0;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #002FA7;">03 / DATABASE & AUTH</div>
    <h3 style="margin-top: 5px;">Supabase (PostgreSQL)</h3>
    <p style="font-size: 14px; margin: 0; color: #555;">Managed serverless database with real-time listeners and secure JWT-based auth.</p>
  </div>
  <div class="card accent" style="margin: 0;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #002FA7;">04 / HOSTING & INFRA</div>
    <h3 style="margin-top: 5px;">Vercel Serverless</h3>
    <p style="font-size: 14px; margin: 0; color: #555;">Serverless edge deployment with automated Git-triggered builds and zero OpEx.</p>
  </div>
</div>

---

# Roadmap

<div class="badge-number">No. 07 / TIMELINE</div>

<div class="vertical-timeline" style="margin-left: 20px;">
  <div class="timeline-node">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">WEEK 1 / PHASE 1</div>
    <h3 style="margin: 5px 0;">Dev Form & Database Setup</h3>
    <p style="font-size: 14px; margin: 0; color: #555;">Database schema configuration, developer daily submission form, and basic REST API controllers.</p>
  </div>
  <div class="timeline-node">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">WEEK 2 / PHASE 2</div>
    <h3 style="margin: 5px 0;">AI Blocker Detection Engine</h3>
    <p style="font-size: 14px; margin: 0; color: #555;">GPT-4o API integration, structured output prompt engineering, and blocker validation model.</p>
  </div>
  <div class="timeline-node">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">WEEK 3 / PHASE 3</div>
    <h3 style="margin: 5px 0;">PM Dashboard Console</h3>
    <p style="font-size: 14px; margin: 0; color: #555;">Real-time blocker alarm workspace, Slack notification gateway, and filterable log view.</p>
  </div>
  <div class="timeline-node" style="margin-bottom: 0;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">WEEK 4 / PHASE 4</div>
    <h3 style="margin: 5px 0;">UAT, Security, & Launch</h3>
    <p style="font-size: 14px; margin: 0; color: #555;">Client user acceptance testing, production edge deployment on Vercel, and project handover.</p>
  </div>
</div>

---

# Team & Investment

<div class="badge-number">No. 08 / BUDGET</div>

<div class="columns">
<div class="column" style="flex: 1.1;">
  <div style="display: flex; flex-direction: column; gap: 8px;">
    <div style="display: flex; justify-content: space-between; border-bottom: 1px solid #0a0a0a; padding-bottom: 8px;">
      <span style="font-weight: 600; font-size: 16px;">Core Development Team</span>
      <span style="font-family: 'JetBrains Mono', monospace; font-size: 16px; color: #002FA7;">1 Fullstack Dev + 0.3 AI + 0.2 QA</span>
    </div>
    <div style="display: flex; justify-content: space-between; border-bottom: 1px solid #0a0a0a; padding-bottom: 8px;">
      <span style="font-weight: 600; font-size: 16px;">Total Engineering Effort</span>
      <span style="font-family: 'JetBrains Mono', monospace; font-size: 16px; color: #002FA7;">112 Man-Hours</span>
    </div>
    <div style="display: flex; justify-content: space-between; border-bottom: 1px solid #0a0a0a; padding-bottom: 8px;">
      <span style="font-weight: 600; font-size: 16px;">MVP Timeline</span>
      <span style="font-family: 'JetBrains Mono', monospace; font-size: 16px; color: #002FA7;">4 Weeks to Live MVP</span>
    </div>
    <div style="display: flex; justify-content: space-between; padding-bottom: 8px;">
      <span style="font-weight: 600; font-size: 16px;">Monthly Operating Cost</span>
      <span style="font-family: 'JetBrains Mono', monospace; font-size: 16px; color: #002FA7;">$5 – $60/month (Free Tier Covers MVP)</span>
    </div>
  </div>
</div>
<div class="column" style="flex: 0.9; display: flex; flex-direction: column; justify-content: center;">
  <div class="card accent" style="margin: 0; text-align: center; padding: 40px 20px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px;">ENGAGEMENT MODEL</div>
    <h2 style="font-size: 40px; margin: 15px 0 5px 0; color: #002FA7; font-weight: 900; line-height: 1;">FIXED PRICE</h2>
    <p style="font-size: 14px; margin: 0; color: #555;">Billed directly upon successful weekly milestone verification</p>
  </div>
</div>
</div>

---

# Payment Schedule

<div class="badge-number">No. 09 / CONTRACT</div>

<div style="display: flex; gap: 20px; width: 100%; margin-top: 30px;">
  <div class="card" style="flex: 1; margin: 0; border-top: 4px solid #002FA7;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 32px; font-weight: 900; color: #002FA7;">30%</div>
    <h3 style="margin-top: 10px;">Milestone 1</h3>
    <p style="font-size: 14px; color: #555; margin-bottom: 0;"><strong>Contract Signing</strong><br>Upon formal project kick-off & development repository setup.</p>
  </div>
  <div class="card" style="flex: 1; margin: 0; border-top: 4px solid #002FA7;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 32px; font-weight: 900; color: #002FA7;">30%</div>
    <h3 style="margin-top: 10px;">Milestone 2</h3>
    <p style="font-size: 14px; color: #555; margin-bottom: 0;"><strong>AI Engine Delivery</strong><br>Upon Week 2 integration & blocker prompt validation tests.</p>
  </div>
  <div class="card accent" style="flex: 1; margin: 0; border-top: 4px solid #002FA7;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 32px; font-weight: 900; color: #002FA7;">40%</div>
    <h3 style="margin-top: 10px;">Milestone 3</h3>
    <p style="font-size: 14px; color: #555; margin-bottom: 0;"><strong>UAT & Launch</strong><br>Upon production environment handover & client sign-off (Week 4).</p>
  </div>
</div>

---

# What's Next (Phase 2)

<div class="badge-number">No. 10 / VISION</div>

<p style="font-size: 15px; color: #555; margin-bottom: 20px;">If MVP succeeds (Adoption &gt;70%, AI accuracy &ge;90%), the system is designed to seamlessly scale to:</p>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; width: 100%;">
  <div class="card" style="margin: 0; padding: 15px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">01 / DISPATCH</div>
    <h3 style="font-size: 14px; margin-top: 5px;">Slack/Teams Integration</h3>
    <p style="font-size: 13px; color: #555; margin: 0;">Developers submit updates directly via native chat slash commands.</p>
  </div>
  <div class="card" style="margin: 0; padding: 15px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">02 / TRACKING</div>
    <h3 style="font-size: 14px; margin-top: 5px;">Jira & Notion Sync</h3>
    <p style="font-size: 13px; color: #555; margin: 0;">Automatically create and update engineering tasks from flagged blockers.</p>
  </div>
  <div class="card" style="margin: 0; padding: 15px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">03 / DATA VIZ</div>
    <h3 style="font-size: 14px; margin-top: 5px;">Trend Analytics</h3>
    <p style="font-size: 13px; color: #555; margin: 0;">Weekly velocity health score dashboards and team bottleneck analytics.</p>
  </div>
  <div class="card accent" style="margin: 0; padding: 15px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #002FA7;">04 / PRIVACY</div>
    <h3 style="font-size: 14px; margin-top: 5px;">Self-Hosted LLM</h3>
    <p style="font-size: 13px; color: #555; margin: 0;">Run local inference models to eliminate third-party API data dependency.</p>
  </div>
</div>

---

# Next Steps

<div class="badge-number">No. 11 / KICKOFF</div>

<div class="columns">
<div class="column card accent" style="flex: 0.9; display: flex; flex-direction: column; justify-content: center; padding: 40px 20px;">
  <div class="dots" style="font-family: 'JetBrains Mono', monospace; opacity: 0.2; font-size: 14px; margin-bottom: 20px; line-height: 1;">
  • • • • •<br>
  • • • • •<br>
  • • • • •
  </div>
  <h2 style="font-size: 32px; font-weight: 900; margin: 0; color: #002FA7; line-height: 1.2;">LET'S BUILD IT.</h2>
</div>
<div class="column" style="flex: 1.1; display: flex; flex-direction: column; justify-content: space-between;">
  <div style="display: flex; flex-direction: column; gap: 15px;">
    <div style="display: flex; gap: 15px; align-items: flex-start;">
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: #002FA7; border: 1px solid #002FA7; padding: 2px 10px;">1</div>
      <div>
        <h3 style="margin: 0 0 5px 0;">Approve Proposal</h3>
        <p style="font-size: 14px; color: #555; margin: 0;">Formal authorization of MVP scope, timeline, and budget.</p>
      </div>
    </div>
    <div style="display: flex; gap: 15px; align-items: flex-start;">
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: #002FA7; border: 1px solid #002FA7; padding: 2px 10px;">2</div>
      <div>
        <h3 style="margin: 0 0 5px 0;">Kick-Off Meeting</h3>
        <p style="font-size: 14px; color: #555; margin: 0;">Schedule the alignment session within 1 week of authorization.</p>
      </div>
    </div>
    <div style="display: flex; gap: 15px; align-items: flex-start;">
      <div style="font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; color: #002FA7; border: 1px solid #002FA7; padding: 2px 10px;">3</div>
      <div>
        <h3 style="margin: 0 0 5px 0;">First Demo Delivery</h3>
        <p style="font-size: 14px; color: #555; margin: 0;">End of Week 1: Presenting a functional dev daily submission form.</p>
      </div>
    </div>
  </div>
</div>
</div>
