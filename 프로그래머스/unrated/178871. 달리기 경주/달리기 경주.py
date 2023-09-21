def solution(players, callings):
    answer = []
    
    player_dict = {}
    for i in range(len(players)):
        if i==0:
            player_dict[players[i]] = [i+1, None, players[i+1]]
        elif i != len(players)-1:
            player_dict[players[i]] = [i+1, players[i-1], players[i+1]]
        else:
            player_dict[players[i]] = [i+1, players[i-1], None]
    
    for name in callings:
        my_num, forward_player, back_player = player_dict[name]
        forward_num, forward2_player, _ = player_dict[forward_player]
        
        player_dict[name] = [my_num-1, forward2_player, forward_player]
        player_dict[forward_player] = [forward_num+1, name, back_player]
        
        if forward2_player is not None:
            forward2_num, forward_3_player, _ = player_dict[forward2_player]
            player_dict[forward2_player] = [forward2_num, forward_3_player, name]
        
        if back_player is not None:
            back_num, _, back2_player = player_dict[back_player]
            player_dict[back_player] = [back_num, forward_player, back2_player]
    
    new_dict = sorted(player_dict.items(), key=lambda x:x[1])
    for name in new_dict:
        answer.append(name[0])
    
    return answer