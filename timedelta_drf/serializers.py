from rest_framework import serializers
from timdelta import helpers


class TimedeltaField(serializers.WritableField):
    error_msg = 'Enter a valid time span: e.g. "3 days, 4 hours, 2 minutes"'

    # DRF 2.x
    def to_native(self, time_delta):
        return helpers.nice_repr(time_delta)

    def from_native(self, value):
        try:
            return helpers.parse(value)
        except TypeError:
            raise serializers.ValidationError(self.error_msg)

    # DRF 3.x
    def to_representation(self, time_delta):
        return self.to_native(time_delta)

    def to_internal_value(self, data):
        return self.from_native(data)
