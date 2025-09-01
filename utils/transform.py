from pyspark.sql.functions import explode, col, array, struct, lit


# Referencia de implementação: https://stackoverflow.com/questions/66130815/how-to-explode-structs-with-pyspark-explode
# Função que retorna Dataframe com coluna do tipo struct explodida
def explode_struct(dataframe, coluna_struct, nome_coluna_chave='chave', nome_coluna_valor='valor'):
    df_transformado  = dataframe.select(
        "*",
        explode(
            #todos os items do explode serão passados para o array
            array(*[
                #Cria struct com estrutura fixa de chave e valor
                struct(
                    lit(item).alias(f"{nome_coluna_chave}"),
                    col(f"{coluna_struct}.{item}").alias(f"{nome_coluna_valor}"),
                )
                for item in dataframe.select(f"{coluna_struct}.*").columns
            ])
        ).alias("coluna_struct")
    ).select("*", "coluna_struct.*").drop("coluna_struct")

    return df_transformado
