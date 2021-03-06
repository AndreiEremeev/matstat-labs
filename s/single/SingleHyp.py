from s import AltHypKind, Hyp


class SingleHyp(Hyp):
    """Single sample hypothesis"""

    def __init__(self, dist, kind=AltHypKind.TWO_SIDED):
        super(SingleHyp, self).__init__(dist, kind)

    def criterion(self, sample):
        pass

    def test(self, sample, alpha):
        _, _, _, result = self.full_test(sample, alpha)
        return result

    def full_test(self, sample, alpha):
        criterion_value = self.criterion(sample)
        crit_left, crit_right = self.critical_values(alpha)

        p_value = self.p_value(criterion_value)

        result = False

        if self.kind == AltHypKind.TWO_SIDED:
            result = (crit_left < criterion_value) and (criterion_value < crit_right)
        if self.kind == AltHypKind.LEFT:
            result = crit_left < criterion_value
        if self.kind == AltHypKind.RIGHT:
            result = criterion_value < crit_right

        return criterion_value, (crit_left, crit_right), p_value, result
