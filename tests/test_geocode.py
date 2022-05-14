from src.geocode.geocode import get_code


class TestGeocode:
    def test_one(self):
        assert get_code("Tribeni", "Rukum West") == 60805

    def test_two(self):
        assert get_code("Tribeni", "Rolpa") == 50206

    def test_three(self):
        assert get_code("Tribeni", "Salyan") == 60909

    def test_four(self):
        assert get_code("Tribeni", "Bajura") == 70109

    def test_five(self):
        assert get_code("Sunkoshi", "sindhupalchowk") == 30212

    def test_six(self):
        assert get_code("Tribeni") == None
