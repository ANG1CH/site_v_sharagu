from flask import Blueprint, render_template, request

from .pars import l2, l3


main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    full_l3 = l3
    filtered_l3 = l3[::11]
    zipped_list = list(zip(full_l3, l2)) if full_l3 and l2 else []
    
    if request.method == 'POST':
        selected_index = int(request.form['selected_value'])

        if selected_index >= len(filtered_l3):
            return render_template('main/error.html'), 400
        
        start_position = selected_index * 11
        
        next_values = full_l3[start_position + 1:start_position + 11]
        corrl_l2 = l2[start_position + 1:start_position + 11]
        zipped_list2 = list(zip(next_values, corrl_l2))
        
        return render_template(
            'main/index.html', 
            l3=full_l3, 
            l2=l2, 
            selected_index=selected_index, 
            next_values=next_values, 
            filtered_l3=filtered_l3,
            corrl_l2=corrl_l2,
            zipped_list2 = zipped_list2
            )
    else:
        return render_template('main/index.html', full_l3=full_l3, l2=l2, selected_index=None, zipped_list=zipped_list, filtered_l3=filtered_l3)

@main.route('/about')
def about():
    return render_template('main/about.html')