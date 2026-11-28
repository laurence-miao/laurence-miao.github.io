---
layout: post
title: My favorite AI agent skills
description: Three collections of AI agent skills for practical software engineering, clearer research papers, and end-to-end academic research.
permalink: /writing/favorite-skills/
date: 2026-11-23
tags: [AI agents, Software engineering, Research writing, Academic research]
back_url: /writing/
back_label: All writing
---

These are three of my favorite collections of AI agent skills, covering software engineering, research writing, and the wider academic research process. Each turns guidance into reusable workflows that an agent can follow for a specific task.

## Matt Pocock’s engineering skills

[Explore mattpocock/skills on GitHub](https://github.com/mattpocock/skills)

Matt Pocock’s collection focuses on the practical work of building and maintaining software: clarifying requirements, planning changes, testing, debugging, and improving architecture. The skills are designed to be small and adaptable, so they can fit into an existing engineering workflow.

A few useful starting points:

- **Clarifying a change:** `grill-with-docs` helps work through requirements, establish shared terminology, and record design decisions.
- **Testing and debugging:** `tdd` guides a red–green–refactor cycle, while `diagnosing-bugs` provides a structured debugging process.
- **Architecture review:** `improve-codebase-architecture` looks for opportunities to simplify interfaces and strengthen module boundaries.

## Research Paper Writing Skills

[Explore Research-Paper-Writing-Skills on GitHub](https://github.com/Master-cai/Research-Paper-Writing-Skills)

This collection focuses on writing machine learning, computer vision, and natural language processing papers. It provides a research-writing workflow with section-specific guidance and templates, from the abstract and introduction through the experiments and conclusion.

Useful tasks include:

- **Structuring a draft:** organizing sections and improving the flow between paragraphs.
- **Checking the argument:** making sure claims are supported by the evidence presented.
- **Reviewing before submission:** reading the paper from a reviewer’s perspective to identify gaps and unclear explanations.

Master-cai curates and packages the skill, drawing primarily on Prof. Peng Sida’s open research notes. The repository explains that attribution and provides setup instructions.

## Academic Research Skills

[Explore academic-research-skills on GitHub](https://github.com/Imbad0202/academic-research-skills)

This suite of Claude Code skills covers the full academic research pipeline: research, writing, peer review, revision, and finalization. The agents handle literature searches, citation formatting, and consistency checks, while the pipeline pauses for the researcher’s confirmation at every stage, so the decisions stay with the author.

A few useful starting points:

- **Planning a paper:** `/ars-plan` works through a paper’s structure in a Socratic dialogue.
- **Reviewing the literature:** `/ars-lit-review` drafts a literature review on a topic, and `deep-research` also supports PRISMA systematic reviews.
- **Simulated peer review:** `academic-paper-reviewer` reviews a manuscript from several perspectives, including journal fit and a devil’s advocate.
- **Integrity checks:** `academic-pipeline` verifies that citations exist and that claims are supported by their sources before and after review.

The suite installs as a Claude Code plugin and is released under CC BY-NC 4.0 for non-commercial use. The repository documents setup, costs, and what data leaves your machine.
