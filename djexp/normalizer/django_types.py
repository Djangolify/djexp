from django.db import models


BYTE_TYPES = [
	models.BigAutoField.__name__,
	models.BinaryField.__name__,
	models.FileField.__name__,
	models.ImageField.__name__,
	models.UUIDField.__name__
]

BOOL_TYPES = [
	models.BooleanField.__name__,
	models.NullBooleanField.__name__
]

STR_TYPES = [
	models.CharField.__name__,
	models.EmailField.__name__,
	models.FilePathField.__name__,
	models.GenericIPAddressField.__name__,
	models.SlugField.__name__,
	models.TextField.__name__,
	models.URLField.__name__
]

TIME_TYPES = [
	models.DateField.__name__,
	models.DateTimeField.__name__,
	models.DurationField.__name__,
	models.TimeField.__name__
]

INT32_TYPES = [
	models.SmallIntegerField.__name__
]

INT64_TYPES = [
	models.AutoField.__name__,
	models.BigIntegerField.__name__,
	models.IntegerField.__name__
]

UINT64_TYPES = [
	models.PositiveIntegerField.__name__
]

UINT32_TYPES = [
	models.PositiveSmallIntegerField.__name__
]

FLOAT64_TYPES = [
	models.DecimalField.__name__,
	models.FloatField.__name__
]
