state = {}

def get_state(element):
    try:
        result = state.get(element)
        return result
    except:
        return False
    
def set_state(id, rec_min='', rec_rec='', result='', trailer_url='', buscando=False):
    state[id] = {
        'rec_min': rec_min,
        'rec_rec': rec_rec,
        'result': result,
        'trailer_url': trailer_url,
        'buscando': buscando
    }