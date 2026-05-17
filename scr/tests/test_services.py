#from scr.services.product_services import ProductServices
import pytest

#@pytest.mark.api 

def test_import_token(auth_token):
    assert auth_token is not None, "auth_token should not be None"
    print("Auth token loaded successfully:", auth_token)

#@pytest.mark.api
def test_import_token_validation(token_validation_outcome):
    assert token_validation_outcome is not None
    print("Token validation outcome:", token_validation_outcome)
#@pytest.mark.api
def test_product_services_import(product_services):
    try:
        product_servicess = product_services.product_details() 

        
        print("Product Services imported and instantiated successfully!", product_servicess)
        assert "id" in product_servicess
        assert "title" in product_servicess
        assert product_servicess["id"] == 1
        assert product_servicess["title"] == "Essence Mascara Lash Princess" 
        assert isinstance(product_servicess["description"], str)  
        print("auth login token:", product_services.auth_login(product_services.username, product_services.password))
    except Exception as e:
        print("Error importing Product Services:", e)
