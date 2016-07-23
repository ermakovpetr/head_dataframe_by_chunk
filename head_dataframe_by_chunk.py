def head_dataframe_by_chunk(df, size_chunk_columns=6, n_rows=2):
    from IPython.core.display import display, HTML

    if type(size_chunk_columns) is list:
        current_column = 0
        for i in size_chunk_columns:
            display(HTML('<style> .df thead tr { background-color: #B0B0B0; } </style>' +
                         df.iloc[:,current_column:current_column+i].head(n_rows).to_html(classes='df')))
            current_column += i
    elif type(size_chunk_columns) is int:
        for i in range(0, df.shape[1], size_chunk_columns):
            display(HTML('<style> .df thead tr { background-color: #B0B0B0; } </style>' +
                         df.iloc[:,i:i+size_chunk_columns].head(n_rows).to_html(classes='df')))
