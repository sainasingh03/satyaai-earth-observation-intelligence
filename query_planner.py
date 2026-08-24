import json
import re

from app.services.nemotron import NemotronService


SYSTEM_PROMPT = """
You are SATYAAI's Earth Observation Query Planner.

Convert natural-language Earth observation questions
into structured analytical plans.

Do not invent satellite measurements.

Allowed analysis types:

vegetation
water
urban_change
agriculture
deforestation
land_cover
change_detection
geospatial
general

Allowed operations:

ndvi
ndwi
temporal_comparison
change_detection
segmentation
area_calculation
buffer
distance
land_cover_classification

Return ONLY valid JSON.

Schema:

{
    "intent": "string",
    "analysis_type": "string",
    "operations": [],
    "location": "string or null",
    "start_year": null,
    "end_year": null,
    "requires_imagery": true,
    "requires_geospatial": false,
    "explanation": "string"
}

Never fabricate measurements.
Never claim analysis has already been executed.
"""


class QueryPlanner:

    def __init__(self):
        self.llm = NemotronService()

    def plan(self, query: str):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": query,
            },
        ]

        response = self.llm.complete(
            messages,
            temperature=0.1,
            max_tokens=1500,
        )

        response = response.strip()

        response = re.sub(
            r"^```json\s*",
            "",
            response,
            flags=re.IGNORECASE,
        )

        response = re.sub(
            r"\s*```$",
            "",
            response,
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            return {
                "intent": "general",
                "analysis_type": "general",
                "operations": [],
                "location": None,
                "start_year": None,
                "end_year": None,
                "requires_imagery": True,
                "requires_geospatial": False,
                "explanation": response,
            }