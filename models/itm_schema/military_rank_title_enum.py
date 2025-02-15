# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Phase 1 Evaluation.  The API is based on the OpenAPI 3.0.3 specification.

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MilitaryRankTitleEnum(str, Enum):
    """
    the branch-specific military rank
    """

    """
    allowed enum values
    """
    PRIVATE_LEFT_PARENTHESIS_RECRUIT_RIGHT_PARENTHESIS = 'Private (Recruit)'
    PRIVATE = 'Private'
    PRIVATE_FIRST_CLASS = 'Private First Class'
    SPECIALIST = 'Specialist'
    CORPORAL = 'Corporal'
    SERGEANT = 'Sergeant'
    STAFF_SERGEANT = 'Staff Sergeant'
    SERGEANT_FIRST_CLASS = 'Sergeant First Class'
    MASTER_SERGEANT = 'Master Sergeant'
    FIRST_SERGEANT = 'First Sergeant'
    SERGEANT_MAJOR = 'Sergeant Major'
    COMMAND_SERGEANT_MAJOR = 'Command Sergeant Major'
    SERGEANT_MAJOR_OF_THE_ARMY = 'Sergeant Major of the Army'
    WARRANT_OFFICER_1 = 'Warrant Officer 1'
    CHIEF_WARRANT_OFFICER_2 = 'Chief Warrant Officer 2'
    CHIEF_WARRANT_OFFICER_3 = 'Chief Warrant Officer 3'
    CHIEF_WARRANT_OFFICER_4 = 'Chief Warrant Officer 4'
    CHIEF_WARRANT_OFFICER_5 = 'Chief Warrant Officer 5'
    ENUM_2ND_LIEUTENANT = '2nd Lieutenant'
    ENUM_1ST_LIEUTENANT = '1st Lieutenant'
    LIEUTENANT = 'Lieutenant'
    CAPTAIN = 'Captain'
    MAJOR = 'Major'
    LIEUTENANT_COLONEL = 'Lieutenant Colonel'
    COLONEL = 'Colonel'
    BRIGADIER_GENERAL = 'Brigadier General'
    MAJOR_GENERAL = 'Major General'
    LIEUTENANT_GENERAL = 'Lieutenant General'
    ARMY_CHIEF_OF_STAFF_LEFT_PARENTHESIS_SPECIAL_RIGHT_PARENTHESIS = 'Army Chief of Staff (special)'
    GENERAL = 'General'
    AIRMAN_BASIC = 'Airman Basic'
    AIRMAN = 'Airman'
    AIRMAN_FIRST_CLASS = 'Airman First Class'
    SENIOR_AIRMAN = 'Senior Airman'
    TECHNICAL_SERGEANT = 'Technical Sergeant'
    SENIOR_MASTER_SERGEANT = 'Senior Master Sergeant'
    FIRST_SERGEANT_SLASH__CHIEF_MASTER_SERGEANT = 'First Sergeant / Chief Master Sergeant'
    CHIEF_MASTER_SERGEANT_OF_THE_AIR_FORCE = 'Chief Master Sergeant of the Air Force'
    AIR_FORCE_CHIEF_OF_STAFF_LEFT_PARENTHESIS_SPECIAL_RIGHT_PARENTHESIS = 'Air Force Chief of Staff (special)'
    SEAMAN_RECRUIT = 'Seaman Recruit'
    SEAMAN_APPRENTICE = 'Seaman Apprentice'
    SEAMAN = 'Seaman'
    PETTY_OFFICER_THIRD_CLASS = 'Petty Officer Third Class'
    PETTY_OFFICER_SECOND_CLASS = 'Petty Officer Second Class'
    PETTY_OFFICER_FIRST_CLASS = 'Petty Officer First Class'
    CHIEF_PETTY_OFFICER = 'Chief Petty Officer'
    SENIOR_CHIEF_PETTY_OFFICER = 'Senior Chief Petty Officer'
    MASTER_CHIEF_PETTY_OFFICER = 'Master Chief Petty Officer'
    MASTER_CHIEF_PETTY_OFFICER_OF_THE_NAVY = 'Master Chief Petty Officer of the Navy'
    MASTER_CHIEF_PETTY_OFFICER_OF_THE_COAST_GUARD = 'Master Chief Petty Officer of the Coast Guard'
    CHIEF_WARRANT_OFFICER = 'Chief Warrant Officer'
    ENSIGN = 'Ensign'
    LIEUTENANT_COMMA__JUNIOR_GRADE = 'Lieutenant, Junior Grade'
    LIEUTENANT_COMMANDER = 'Lieutenant Commander'
    COMMANDER = 'Commander'
    REAR_ADMIRAL_LEFT_PARENTHESIS_LOWER_HALF_RIGHT_PARENTHESIS = 'Rear Admiral (Lower Half)'
    REAR_ADMIRAL_LEFT_PARENTHESIS_UPPER_HALF_RIGHT_PARENTHESIS = 'Rear Admiral (Upper Half)'
    VICE_ADMIRAL = 'Vice Admiral'
    CHIEF_OF_NAVAL_OPERATIONS_LEFT_PARENTHESIS_SPECIAL_RIGHT_PARENTHESIS = 'Chief of Naval Operations (special)'
    COMMANDANT_OF_THE_COAST_GUARD_LEFT_PARENTHESIS_SPECIAL_RIGHT_PARENTHESIS = 'Commandant of the Coast Guard (special)'
    ADMIRAL = 'Admiral'
    LANCE_CORPORAL = 'Lance Corporal'
    GUNNERY_SERGEANT = 'Gunnery Sergeant'
    MASTER_GUNNERY_SERGEANT = 'Master Gunnery Sergeant'
    SERGEANT_MAJOR_OF_THE_MARINE_CORPS = 'Sergeant Major of the Marine Corps'
    WARRANT_OFFICER = 'Warrant Officer'
    COMMANDANT_OF_THE_MARINE_CORPS = 'Commandant of the Marine Corps'
    SPECIALIST_1 = 'Specialist 1'
    SPECIALIST_2 = 'Specialist 2'
    SPECIALIST_3 = 'Specialist 3'
    SPECIALIST_4 = 'Specialist 4'
    CHIEF_MASTER_SERGEANT = 'Chief Master Sergeant'
    CHIEF_MASTER_SERGEANT_OF_THE_SPACE_FORCE = 'Chief Master Sergeant of the Space Force'
    CHIEF_OF_SPACE_OPERATIONS = 'Chief of Space Operations'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MilitaryRankTitleEnum from a JSON string"""
        return cls(json.loads(json_str))


