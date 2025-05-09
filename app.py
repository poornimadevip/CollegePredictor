from flask import Flask, request, render_template, send_file
import pandas as pd

app = Flask(__name__)
# filepath = 'institutes.xlsx'
filepath = 'RankList.xlsx'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rank = int(request.form['rank'])
        # selected_gender = request.form['gender']
        selected_programs = request.form.getlist('academic_programs')
        selected_institutes = request.form.getlist('institutes')
        selected_quota = request.form.getlist('quotas')
        selected_year = request.form.getlist('year')
        selected_round = request.form.getlist('rounds')


        # Load data from Excel
        df = pd.read_excel(filepath)
        academic_programs = df['Academic Program Name'].unique()
        institutes = df['Institute'].unique()
        quota= df['Quota'].unique()

        # Filter based on rank conditions
        if rank>0:
            filtered_df = df[(df['Opening Rank'] <= rank) & (df['Closing Rank'] >= rank)]
            # if filtered_df.empty:
            #     filtered_df = df[(df['Opening Rank'] > rank)]
        else:
            filtered_df = df
        
        # Filter based on gender if selected
        # if selected_gender:
        #     filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]

    
        if selected_programs:
            filtered_df = filtered_df[filtered_df['Academic Program Name'].isin(selected_programs)]
        
        if selected_institutes:
            filtered_df = filtered_df[filtered_df['Institute'].isin(selected_institutes)]

        if selected_quota:
            filtered_df = filtered_df[filtered_df['Quota'].isin(selected_quota)]
        
        if selected_year:
            filtered_df = filtered_df[filtered_df['Year'].isin(selected_year)]
        if selected_round:  
            filtered_df = filtered_df[filtered_df['Round'].isin(selected_round)]
        
        # Sort results by opening rank
        filtered_df = filtered_df.sort_values(by=['Year','Round','Opening Rank'], ascending=[False, True, True])

        return render_template('index.html', academic_programs=academic_programs,
                               tables=[filtered_df.to_html(classes='data')], 
                               titles=filtered_df.columns.values,
                               institutes=institutes,
                               quotas=quota)

    # GET request to load programs for selection
    df = pd.read_excel(filepath)
    academic_programs = df['Academic Program Name'].unique()

    institutes = df['Institute'].unique()
    quota= df['Quota'].unique()
    
    return render_template('index.html', academic_programs=academic_programs, institutes=institutes, quotas=quota)

@app.route('/download', methods=['POST'])
def download():
    rank = int(request.form['rank'])
    selected_programs = request.form.getlist('academic_programs')

    # Load data from Excel
    df = pd.read_excel(filepath)

    # Filter based on rank conditions
    filtered_df = df[(df['Opening Rank'] <= rank) & (df['Closing Rank'] >= rank)]

    if selected_programs:
        filtered_df = filtered_df[filtered_df['Academic Program Name'].isin(selected_programs)]

    # Save result as Excel file
    output_file = 'filtered_results.xlsx'
    filtered_df.to_excel(output_file, index=False)
    
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)