from django.db import models

class Table(models.Model):
    
    CASE_SUBMITTED = models.CharField(null=True)
    CASE_STATUS = models.CharField(null=True)
    VISA_CLASS = models.CharField(null=True)
    
    EMPLOYER_NAME = models.CharField(null=True)
    EMPLOYER_ADDRESS = models.CharField(null=True)
    EMPLOYER_CITY = models.CharField(null=True)
    EMPLOYER_STATE = models.CharField(null=True)
    EMPLOYER_POSTAL_CODE = models.CharField(null=True)
    EMPLOYER_COUNTRY = models.CharField(null=True)
    EMPLOYER_PHONE = models.CharField(null=True)
    
    AGENT_ATTORNEY_NAME = models.CharField(null=True)
    JOB_TITLE = models.CharField(null=True)
    SOC_CODE = models.CharField(null=True)
    SOC_NAME = models.CharField(null=True)
    NAIC_CODE = models.CharField(null=True)
    TOTAL_WORKERS = models.CharField(null=True)
    
    PREVAILING_WAGE = models.CharField(null=True)
    PW_UNIT_OF_PAY = models.CharField(null=True)
    PW_WAGE_SOURCE = models.CharField(null=True)
    PW_SOURCE_YEAR = models.CharField(null=True)
    WAGE_RATE_OF_PAY_FROM = models.CharField(null=True)
    WAGE_RATE_OF_PAY_TO = models.CharField(null=True)
    WAGE_UNIT_OF_PAY = models.CharField(null=True)
    
    class Meta:
        app_label = 'final1'
        
    def _str_(self):
        return self.title