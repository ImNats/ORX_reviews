@REM turn on env
call ./env/Scripts/Activate.bat


@REM --------------------/ Install python /-------------------------------------------
@REM install python


@REM --------------------/ Install libs /-------------------------------------------
@REM lib for unittest:
pip install pytest


@REM --------------------/ Libs for Data Science /---------------------------------------------
@REM lib for tables
pip install pandas

@REM lib for PostgreSQL:
pip install psycopg2-binary
@REM lib for SQL:
pip install sqlalchemy


pause
