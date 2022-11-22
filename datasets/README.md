# Datasets
| filename | description |
|-|-|
| dataset_unmodified.csv | original, unmodified data |
| dataset_attributes_added.csv | attributes added based on choices below |
| dataset.csv | attributes added and attributes they were derived from removed |

# Binning Choices
| new attribute | derived from |
|-|-|
| BMI_bin | BMI |
| MentHlth_bin | MentHlth |
| PhysHlth_bin | PhysHlth |
| Diabetes_bin | Diabetes |

# Bin Values
## BMI
The data set contains a wide range of values. The CDC defines the following categories:
| Value | Weight Status | BMI |
|-|-|-|
| 0 | Underweight | <18.5 |
| 1 | Healthy Weight | 18.5-24.9 |
| 2 | Overweight | 25-29.9 |
| 3 | Obesity | >30 |

## Mental Health
The number of days in the last month with "bad" mental health.
| Value | Category | Days |
|-|-|-|
| 0 | Low | 1-10 |
| 1 | Medium | 11-20 |
| 2 | High | 21+ |

## Physical Health
The number of days in the last month with "bad" physical health.
| Value | Category | Days |
|-|-|-|
| 0 | Low | 1-10 |
| 1 | Medium | 11-20 |
| 2 | High | 21+ |

## Diabetes
| Value | |
|-|-|
| 0 | No |
| 1 | Yes or Yes, but female during pregnancy |
