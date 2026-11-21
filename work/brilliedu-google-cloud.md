---
layout: work
title: Scaling workforce training with generative AI
permalink: /projects/brilliedu-google-cloud/
description: A Google Cloud solution I designed for a Customer Engineer interview, using AI and human review to turn partner materials into approved learning plans.
kind: Interview solution design
period: Google Cloud Customer Engineer
role: Solution designer and interview candidate
focus: Google Cloud architecture and generative AI
visual: brilliedu
presentation_url: https://docs.google.com/presentation/d/1SI7tqlC9ozOQBpEd4n2xd3TPftN-wGWsco5wZLYWkBE/edit?usp=sharing
slide_count: 22
---

## Interview context

I designed this solution for a Google Cloud Customer Engineer (CE) interview and passed the interview. The presentation uses **BrilliEdu, a hypothetical workforce-training platform**, as its customer scenario.

## The challenge

BrilliEdu's MVP runs its application, background jobs, and PostgreSQL on one virtual machine. Growth brings more learners and partner materials, while a small delivery team must preserve reliable access and human support.

## The proposed solution

- **Material onboarding:** Cloud Run, Eventarc, and Workflows coordinate uploads and processing. Document AI, Speech-to-Text, and Gemini help interpret source material.
- **Content curation:** scoped retrieval combines approved evidence with Gemini to suggest learning-outcome mappings. Cloud Storage and Cloud SQL retain source versions and structured results.
- **Learning delivery:** curators publish versioned curriculum packs; trainers review and approve individual learning plans before delivery.

## Design priorities

The proposal keeps human approval at key decisions, tracks source permissions and versions, and plans a phased migration. Recovery, cost controls, monitoring, and accountable owners support the small team's operations.

The linked presentation includes the customer scenario, architecture diagrams, and delivery workflows.
