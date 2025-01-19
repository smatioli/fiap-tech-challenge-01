import pandas as pd
from app.db.connection import SessionLocal
from app.db.models import ProductionDB, ProcessingDB, CommercializationDB, ImportationDB, ExportationDB
from sqlalchemy.orm import Session


def load_csv_to_database_async(csv_file, model_class, column_mapping):
    session: Session = SessionLocal()
    
    try:               
        df = pd.read_csv(csv_file)               
        df.rename(columns=column_mapping, inplace=True)
        
        instances = [
            model_class(**row.to_dict()) for _, row in df.iterrows()
        ]

        session.add_all(instances)
        session.commit()        
        print(f"Dados do arquivo {csv_file} carregados com sucesso na tabela '{model_class.__tablename__}'.")

    except Exception as e:
        session.rollback()
        print(f"Erro ao carregar dados do arquivo {csv_file} para a tabela '{model_class.__tablename__}': {str(e)}")
    finally:
        session.close()

def main():   
    mappings = {
        ProductionDB: {
            'produto': 'product',
            'quantidade': 'quantity',
            'ano': 'year'
        },
        CommercializationDB: {
            'produto': 'product',
            'quantidade': 'quantity',
            'ano': 'year'
        },
        ImportationDB: {
            'paises': 'country',
            'quantidade': 'quantity',
            'valor': 'value',
            'ano': 'year',
            'derivado_uva': 'grape_derivative'
        },
        ExportationDB: {
            'paises': 'country',
            'quantidade': 'quantity',
            'valor': 'value',
            'ano': 'year',
            'derivado_uva': 'grape_derivative'
        },
        ProcessingDB: {
            'classificacao_uva': 'grape_classification',
            'cultivar': 'grape_cultivar',
            'quantidade': 'quantity',
            'ano': 'year'
        }
    }
    
    csv_files_and_models = [
        ('app/files/opt_02.csv', ProductionDB),
        ('app/files/opt_03.csv', ProcessingDB),
        ('app/files/opt_04.csv', CommercializationDB),
        ('app/files/opt_05.csv', ImportationDB),
        ('app/files/opt_06.csv', ExportationDB)
    ]

    # carregar os dados de cada arquivo csv na tabela correspondente
    for csv_file, model in csv_files_and_models:
        load_csv_to_database_async(csv_file, model, mappings[model])

if __name__ == '__main__':
    main()