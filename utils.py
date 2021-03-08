import chess
import numpy as np

def who(player):
    return "White" if player == chess.WHITE else "Black"

def reduced_fen(fen):
    return " ".join(fen.split(" ")[:-2])

def get_moves(analysis, lookup_fen):
    keys = list(analysis.keys())
    red_fen = reduced_fen(lookup_fen)
    
    indexes = [i for i,(fen,san) in enumerate(keys) if fen == red_fen]
    
    return [analysis[keys[x]] for x in indexes]
    
def get_info_sorted(analysis):
    
    sort_val = np.array([analysis[x]['count']*100000 - analysis[x]['diff'] for x in analysis])
    sort_order = np.argsort(-sort_val)

    info = np.array([analysis[x] for x in analysis])[sort_order]
    
    return info