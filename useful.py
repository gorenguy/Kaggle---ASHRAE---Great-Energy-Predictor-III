import pandas as pd

def downcast_dtypes(df):
    '''
        Changes column types in the dataframe: 
                
                `float64` type to `float32`
                `int64`   type to `int32`
    '''
    
    # Select columns to downcast
    float_cols = [c for c in df if df[c].dtype == "float64"]
    int_cols =   [c for c in df if (df[c].dtype == "int64") | (df[c].dtype == "int32") | (df[c].dtype == "int16")]
    
    usigned_mask = (df[int_cols]>=0).all(axis=0)
    int_cols_usigned = df[int_cols].columns[~usigned_mask]
    int_cols_signed = df[int_cols].columns[usigned_mask]
    
    # Downcast
    df[float_cols] = df[float_cols].apply(pd.to_numeric, downcast='float')
    df[int_cols_usigned]   = df[int_cols_usigned].apply(pd.to_numeric, downcast='unsigned')
    df[int_cols_signed]   = df[int_cols_signed].apply(pd.to_numeric, downcast='integer')
#     df[float_cols] = df[float_cols].astype(np.float32)
#     df[int_cols]   = df[int_cols].astype(np.int32)
    
    return df