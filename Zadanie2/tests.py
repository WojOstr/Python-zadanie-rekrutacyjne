import zadanie2
import pytest

@pytest.mark.parametrize('pesel',['80122691715','801226917', '801226a171,','36337953780', '57052629141','45760503219', '64656152866','04241092754','21054038610'])
def test_validate_pesel_wrong(pesel):
    #given
    corr_val = "Pesel number correct!"

    #when
    res = zadanie2.validate_pesel(pesel)
        
    #then
    assert res == corr_val, res
