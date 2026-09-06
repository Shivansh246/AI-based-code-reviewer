# Security Review Prototype

A VS Code security-review prototype combining static analysis,
LLM semantic analysis, dependency/CVE checks, risk scoring,
voice interaction, adaptive feedback, multimodal experiments,
and explainable findings.

## Project Goal

Build a working prototype over 8 weeks.

The project focuses on integrating existing libraries and
pretrained models rather than training a large model from scratch.

## Week 1 — ML Foundation

### Completed

- Set up Python virtual environment
- Installed CPU-only PyTorch
- Installed torchvision
- Installed torchaudio
- Verified PyTorch installation

### Current Focus

- Learn PyTorch tensors
- Understand model and inference basics
- Learn embeddings
- Learn JSON structured model output
- Define common vulnerability-result schema

## Environment

- Python
- PyTorch
- torchvision
- torchaudio

## Development Log

### Day 1

Set up the Python environment and installed CPU-only PyTorch.

The initial installation attempted to download CUDA/NVIDIA
dependencies, so the environment was recreated and PyTorch
was installed using the CPU-only package index.