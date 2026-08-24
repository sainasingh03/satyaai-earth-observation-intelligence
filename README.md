# 🌍 SATYAAI — Earth Observation Intelligence

<h1 align="center">🌷 SATYAAI</h1>

<h3 align="center">Ask the Earth. Understand the Change.</h3>

<p align="center">
  <strong>AI-Powered Earth Observation & Geospatial Intelligence Platform</strong>
</p>

<p align="center">
  Turning satellite imagery, geospatial data and environmental signals
  into understandable, explainable and actionable intelligence.
</p>

<p align="center">
  <img src="./docs/satyaai-hero.png" alt="SATYAAI Earth Observation Intelligence" width="100%">
</p>

<p align="center">
  <em>
    A natural-language interface for exploring Earth observation intelligence.
  </em>
</p>

---

## 📌 Project Information

| Field | Details |
|---|---|
| Project | SATYAAI |
| Full Name | SATYAAI — Earth Observation Intelligence |
| Tagline | Ask the Earth. Understand the Change. |
| Domain | Artificial Intelligence / Machine Learning |
| Sub-Domain | Earth Observation / GIS / Computer Vision |
| Problem Statement | SIH26167 — SatQuery AI — ISRO |
| Frontend | React + TypeScript + Vite |
| Backend | Python + FastAPI |
| AI/ML | PyTorch, Transformers, OpenCV, NumPy, Pandas, Scikit-learn |
| Geospatial | Rasterio, GeoPandas, Shapely |
| Database | SQLite + SQLAlchemy |
| Maps | Leaflet / MapLibre |
| Optional LLM | NVIDIA NIM / Nemotron / Ollama |
| Development | VS Code |
| Version Control | Git + GitHub |

---

# 🌍 1. Overview

Earth observation satellites continuously capture enormous amounts of information about our planet.

Satellite imagery can provide valuable information about:

- Forests
- Agriculture
- Water bodies
- Rivers
- Urban development
- Land cover
- Vegetation
- Environmental changes
- Disaster-affected regions
- Coastal regions
- Ecosystems

However, extracting useful information from satellite data is often difficult.

A user may need knowledge of:

- Remote sensing
- GIS
- Raster processing
- Satellite bands
- Spectral indices
- Coordinate systems
- Spatial analysis
- Image processing
- Machine learning
- Change detection

This creates a gap between **Earth observation data** and **people who need to understand that data**.

SATYAAI is designed to reduce this gap.

---

# 💡 2. What is SATYAAI?

**SATYAAI** is an AI-powered Earth Observation Intelligence platform that allows users to ask questions about geographical and environmental changes using **natural language**.

Instead of manually configuring a complicated GIS workflow, a user can ask:

> "Where has vegetation decreased near river basins in Kerala between 2022 and 2026?"

SATYAAI interprets the query and converts it into structured spatial and analytical intent.

The system can then combine:

```text
Natural Language
        ↓
AI Query Understanding
        ↓
Earth Observation Data
        ↓
Computer Vision
        ↓
Geospatial Analysis
        ↓
Change Detection
        ↓
Evidence
        ↓
Explainable Result
        ↓
Interactive Earth Report



🚨 3. Problem Statement
The Problem

Earth observation systems generate huge amounts of satellite imagery and geospatial information.

Although this information is extremely valuable, accessing meaningful intelligence from it often requires specialized knowledge.

Traditional workflows may require users to:

Find appropriate satellite datasets.
Select a geographic region.
Select a time period.
Download imagery.
Preprocess raster data.
Select relevant spectral bands.
Calculate vegetation or water indices.
Perform spatial analysis.
Compare multiple time periods.
Detect changes.
Visualize results.
Interpret the output.

For non-GIS users, this workflow can be complex and time-consuming.

Core Problem

How can we make complex Earth observation and geospatial analysis accessible through a simple natural-language interface while preserving scientific evidence and explainability?

🎯 4. Proposed Solution

SATYAAI introduces an AI-powered natural-language interface over Earth observation workflows.

A user simply asks a question.

For example:

Where has vegetation decreased near rivers?

SATYAAI identifies:

Target:
Vegetation

Operation:
Change Detection

Direction:
Decrease

Spatial Feature:
River

Potential Analysis:
NDVI

Time:
User-selected period

The system then builds an appropriate analytical workflow.

🌷 5. Core Concept

The SATYAAI workflow can be represented as:

                     🌷 SATYAAI
                          │
                          ▼
                  Ask the Earth
                          │
                          ▼
              Natural Language Query
                          │
                          ▼
                  AI Query Planner
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
       Vision AI                    Geo AI / GIS
            │                           │
            ▼                           ▼
    Satellite Analysis          Spatial Analysis
            │                           │
            └─────────────┬─────────────┘
                          ▼
                   Change Detection
                          │
                          ▼
                    Evidence Layer
                          │
                          ▼
                  Explainable AI
                          │
                          ▼
                    Earth Report
⭐ 6. What Makes SATYAAI Different?

SATYAAI is not simply an AI chatbot.

The core idea is to connect:

AI
+
Computer Vision
+
Satellite Data
+
GIS
+
Spatial Reasoning
+
Change Detection
+
Explainability

Instead of only generating text, the system is designed to connect natural-language questions to measurable Earth observation analysis.

🔥 7. Key Features
🗣️ 7.1 Natural Language Earth Queries

Users can ask questions using ordinary language.

Examples:

Show vegetation loss in the Western Ghats.
Where has water coverage decreased?
Find environmental changes near river basins.
Show areas where vegetation decreased between 2022 and 2026.
Find regions with significant land-cover changes.
🤖 7.2 AI Query Understanding

The AI layer converts natural-language queries into structured intent.

Example:

Input
Where has vegetation decreased near river basins
in Kerala between 2022 and 2026?
Parsed Intent
Location:
Kerala

Target:
Vegetation

Change:
Decrease

Geographic Feature:
River Basin

Time Range:
2022 → 2026

Analysis:
NDVI / Multi-temporal analysis
🛰️ 7.3 Satellite Image Analysis

SATYAAI is designed to work with Earth observation imagery.

Potential inputs include:

Multispectral imagery
Raster imagery
GeoTIFF
Satellite-derived datasets
Processed Earth observation layers

The system can perform preprocessing before analysis.

🌿 7.4 Vegetation Analysis

Vegetation analysis can use spectral indices such as NDVI.

NDVI
NDVI = (NIR - RED) / (NIR + RED)

The system can compare vegetation indicators across time.

Example:

2022
 ↓
NDVI
 ↓
2026
 ↓
NDVI
 ↓
Difference
 ↓
Potential Vegetation Change
💧 7.5 Water Analysis

The platform can be extended to analyze water-related changes.

Possible workflows include:

Water extent
Water coverage
Water-body change
Wetland monitoring
River-adjacent analysis
🏙️ 7.6 Land-Cover Analysis

Potential categories include:

Vegetation
Water
Built-up Area
Bare Soil
Agricultural Land
Forest

Computer vision and spectral analysis can help identify spatial patterns.

🔄 7.7 Change Detection

SATYAAI can compare Earth observation data from different time periods.

Satellite Image — Time A
          │
          ▼
     Preprocessing
          │
          ▼
     Feature Extraction
          │
          ▼
     ┌──────────────┐
     │ Comparison   │
     └──────┬───────┘
            │
            ▼
     Change Detection
            ▲
            │
     ┌──────┴───────┐
     │ Feature      │
     │ Extraction   │
     └──────▲───────┘
            │
       Preprocessing
            │
            ▲
Satellite Image — Time B
🗺️ 7.8 Interactive GIS Explorer

Analysis results can be visualized on an interactive map.

The map can display:

Satellite imagery
Analysis boundaries
Change regions
Raster layers
Vector layers
Geographic features
Query results

The objective is to answer:

Where did the change happen?

rather than only:

How much change happened?

📊 7.9 Evidence-Based Results

SATYAAI aims to present evidence with every analysis.

A result can contain:

WHAT?
Vegetation change

WHERE?
Detected region

WHEN?
Selected comparison period

HOW MUCH?
Computed affected area

EVIDENCE?
Spectral / spatial measurements

CONFIDENCE?
Model-derived or analysis-derived value
🔍 7.10 Explainable AI

The system is designed to explain analytical results.

Example:

Vegetation decline was detected in the selected
region based on the change in the vegetation index
between the selected observation periods.

The highlighted regions represent areas where the
computed index difference exceeded the selected
change threshold.

The objective is to avoid presenting unexplained AI outputs.

🧠 7.11 AI + GIS + Computer Vision

SATYAAI combines multiple technical disciplines.

                    SATYAAI
                       │
       ┌───────────────┼───────────────┐
       │               │               │
       ▼               ▼               ▼
      AI              GIS            Vision
       │               │               │
       ▼               ▼               ▼
     NLP/LLM       Spatial Ops     Image Analysis
       │               │               │
       └───────────────┼───────────────┘
                       │
                       ▼
              Earth Intelligence
🏗️ 8. System Architecture
┌─────────────────────────────────────────────────────────────┐
│                       SATYAAI                              │
│              Earth Observation Intelligence                │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │   React Frontend   │
                    │ TypeScript + Vite  │
                    │   Tailwind CSS     │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │     FastAPI        │
                    │    REST API        │
                    └──────────┬─────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      ┌────────────┐    ┌────────────┐    ┌────────────┐
      │ AI Query   │    │ Vision AI  │    │  Geo AI    │
      │ Planner    │    │ Pipeline   │    │ / GIS      │
      └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
            │                 │                 │
            ▼                 ▼                 ▼
       NLP / LLM          OpenCV             Rasterio
       Nemotron           PyTorch            GeoPandas
       Ollama             NumPy              Shapely
            │                 │                 │
            └─────────────────┼─────────────────┘
                              ▼
                     Change Detection
                              │
                              ▼
                      Evidence Engine
                              │
                              ▼
                       Explainable AI
                              │
                              ▼
                        Earth Report
🔬 9. AI/ML Pipeline

The AI/ML pipeline is divided into multiple stages.

User Query
    ↓
Text Preprocessing
    ↓
Intent Extraction
    ↓
Entity Recognition
    ↓
Spatial Parameter Extraction
    ↓
Temporal Parameter Extraction
    ↓
Analysis Planning
    ↓
Earth Observation Processing
    ↓
Computer Vision / ML
    ↓
Change Detection
    ↓
Evidence Generation
    ↓
Natural Language Explanation
🧠 10. Natural Language Processing

The NLP layer can extract:

Location
Kerala
Western Ghats
Delhi
Ganga Basin
Target
Vegetation
Water
Forest
Urban Area
Agriculture
Operation
Find
Compare
Detect
Show
Analyze
Monitor
Change
Increase
Decrease
Loss
Growth
Expansion
Reduction
Time
2022
2026
2022–2026
Last 5 years
👁️ 11. Computer Vision Pipeline

The computer vision layer can include:

Input Raster
     ↓
Image Validation
     ↓
Preprocessing
     ↓
Normalization
     ↓
Band Processing
     ↓
Feature Extraction
     ↓
Segmentation / Classification
     ↓
Spatial Mask
     ↓
Change Analysis

Libraries:

OpenCV
PyTorch
NumPy
Scikit-learn
🗺️ 12. Geospatial Pipeline

The GIS pipeline can include:

Geographic Query
       ↓
Coordinate Extraction
       ↓
Spatial Boundary
       ↓
Raster Selection
       ↓
Raster Processing
       ↓
Geometry Operations
       ↓
Area Calculation
       ↓
Spatial Filtering
       ↓
Map Layer

Technologies:

Rasterio
GeoPandas
Shapely
Leaflet
MapLibre
📐 13. Spatial Analysis

SATYAAI can support operations such as:

Buffer
Intersection
Distance
Area
Polygon Filtering
Bounding Box
Coordinate Transformation
Raster Masking

Example:

Find vegetation change
within 5 km
of a river

The query can become:

Target:
Vegetation

Change:
Decrease

Feature:
River

Buffer:
5 km
🔄 14. Change Detection

A simplified change detection workflow:

Image A
  ↓
Feature Extraction
  ↓
Feature Map A

Image B
  ↓
Feature Extraction
  ↓
Feature Map B

Feature Map A
       +
Feature Map B
       ↓
Difference
       ↓
Threshold / Model
       ↓
Change Mask
       ↓
Spatial Polygon
       ↓
Map Visualization
📈 15. Evaluation Metrics

Models and analytical pipelines should be evaluated using measurable metrics.

Possible metrics:

Metric	Purpose
Precision	Correct positive predictions
Recall	Detection coverage
F1 Score	Precision-recall balance
IoU	Segmentation overlap
Latency	Processing speed
MAE	Regression error
RMSE	Numerical error

SATYAAI should never claim an accuracy percentage unless that percentage has been measured on an appropriate dataset.

🛡️ 16. AI Reliability

A major design principle is:

Never fake AI.

SATYAAI distinguishes between:

DEMO

Preconfigured demonstration data.

BASELINE

Real computational methods such as:

NDVI calculation
Raster operations
OpenCV
Statistical comparison
Threshold-based change detection
MODEL-POWERED

Actual trained or hosted machine-learning models.

The application should clearly identify which mode produced a result.
