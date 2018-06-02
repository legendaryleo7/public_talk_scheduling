## Congregation: ##
* CongregationGuid: uuid
* Name: string
* Address: string
* City: string
* State: string
* PostalCode: int
* Country: enum
* CongregationType: enum
* Language: enum
* MeetingDay: enum
* MeetingTime: time

## HomeCongregation: ## 
* CongregationGuid: uuid

## CongregationMember: ## 
* CongregationMemberGuid: uuid
* CongregationGuid: uuid
* IsElder: boolean
* IsServant: boolean
* IsMale: bool (default=true)
* IsSpeaker: bool
* IsTalkCoordinator: bool
* Phone1: string
* Phone1Type: enum
* Phone2: string
* Phone2Type: enum
* Phone3: string
* Phone3Type: enum

## SpeakerTalk: ## 
* SpeakerTalkGuid: uuid
* CongregationMemberGuid: uuid
* OutlineNumber:int 
* Language: enum

## Talk: ## 
* OutlineNumber: int
* Theme: string

## MeetingOccurance: ##
* MeetingOccuranceGuid: uuid
* CongregationGuid: uuid
* CongregationMemberGuid: uuid
* Date: datetime
* HasOverridenDatetime: boolean
* SpeakerWillAcceptHospitality: boolean?
* AssignedHospitalityGroupGuid: uuid

## MeetingOccuranceOverride: ## 
* MeetingOccuranceGuid: uuid
* OriginalDateTime: datetime
* NewDateTime: datetime

## HospitalityGroup: ## 
* HospitalityGroupGuid:uuid
* HospitalityGroupTypeGuid: uuid
* PrimaryCongregationMemberGuid: uuid
* SecondaryCongregationMemberGuid: uuid

## HospitalityGroupType ##
* HospitalityGroupTypeId: uuid
* HospitalityGroupTypeName: string
