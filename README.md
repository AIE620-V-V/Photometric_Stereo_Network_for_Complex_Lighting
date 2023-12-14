# Photometric_Stereo_Network_for_Complex_Lighting
Sogang Univ AIE6202 project . Photometric Stereo Network for Complex Lighting
개요
이 프로젝트는 복잡한 조명 환경 하에서 보정되지 않은 광도 스테레오 문제를 해결하기 위한 혁신적인 접근법을 제시합니다. 여기에는 **WiDiNet (Wild-to-Directional Network)**과 **SCPS-NIR (Self-Calibrating Photometric Stereo by Neural Inverse Rendering)**이 포함됩니다.

이론적 배경
WiDiNet은 복잡한 환경 조명을 단순한 방향성 조명으로 변환하는 프로세스이며, SCPS-NIR은 조명과 표면 정규를 추정하는 역렌더링 접근 방식을 사용합니다.

주요 특징
재조명 모듈: 다양한 방향성 조명 하에서 이미지를 생성합니다.
WtD 모듈 (Wild-to-Directional): 이미지에서 환경 조명을 추출하여 방향성 광원 이미지로 변환합니다.
데이터셋과 평가: 다양한 데이터셋에서 뛰어난 성능을 입증하였습니다.
환경 설정
WiDiNet과 SCPS-NIR에 대한 환경 설정은 각각의 GitHub 리포지토리를 참고하여 진행해야 합니다.

WiDiNet GitHub: IAN Repository (https://github.com/NK-CS-ZZL/IAN)
SCPS-NIR GitHub: SCPS-NIR Repository (https://github.com/junxuan-li/SCPS-NIR)

실험 결과
WiDiNet과 SCPS-NIR은 PS-WL 데이터셋과 DiLiGenT 벤치마크에서 우수한 성능을 보여주었습니다. 아래는 평균 MAE를 나타내는 표입니다.
### PS-WL 데이터셋

| 방법 | Dragon | Duck | Game | Mask | Ornament | Pig | Ring | Ring2 | 평균 MAE |
|------|--------|------|------|------|----------|-----|------|-------|----------|
| GCNet [6] | 37.70 | 56.41 | 32.75 | 31.89 | 52.60 | 27.96 | 62.51 | 67.83 | 46.21 |
| SCPS-NIR [12] | 78.84 | 52.11 | 42.86 | 59.49 | 49.40 | 41.52 | 54.92 | 46.31 | 53.18 |
| UniPS [10] | 24.50 | 35.03 | 17.15 | 13.15 | 27.10 | 20.71 | 39.24 | 28.28 | 25.65 |
| WtD + SCPS-NIR [12] | 48.23 | 35.43 | 12.03 | 11.05 | 32.68 | 15.08 | 64.58 | 30.73 | 31.23 |
| WiDiNet + SCPS-NIR [12] | 17.91 | 34.98 | 12.10 | 7.78 | 29.63 | 15.11 | 32.34 | 29.24 | 22.39 |

### DiLiGenT 벤치마크

| 방법 | Ball | Bear | Buddha | Cat | Cow | Goblet | Harvest | Pot1 | Pot2 | Reading | 평균 MAE |
|------|------|------|--------|-----|-----|--------|---------|------|------|---------|----------|
| SCPS-NIR [12] | 1.24 | 3.82 | 9.28 | 4.72 | 5.53 | 7.12 | 14.96 | 6.73 | 6.50 | 10.54 | 7.05 |
| UniPS [10] | 6.41 | 7.43 | 20.88 | 11.23 | 7.72 | 28.23 | 23.67 | 11.41 | 9.80 | 20.08 | 14.69 |
| WtD + SCPS-NIR [12] | 4.15 | 2.89 | 9.70 | 10.14 | 4.54 | 8.73 | 15.92 | 5.30 | 4.55 | 10.88 | 7.68 |
| WiDiNet + SCPS-NIR [12] | 0.49 | 2.19 | 9.47 | 5.02 | 4.08 | 7.25 | 14.25 | 5.99 | 3.78 | 10.09 | 6.26 |

전체 프로세스 구조
![image](https://github.com/AIE620-V-V/Photometric_Stereo_Network_for_Complex_Lighting/assets/46189116/e94f1221-020e-4226-89a4-55c66c87318b)

![image](https://github.com/AIE620-V-V/Photometric_Stereo_Network_for_Complex_Lighting/assets/46189116/495d55ba-d9b0-4048-8a05-0abfe603bd48)


참고문헌 및 추가 자료
