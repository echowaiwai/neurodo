from semantic_coherence.semantic_coherence import index_file, index_string

def ave_of_mins(l, chunk_size):
    chunked = (l[x:x+chunk_size] for x in range(0, len(l), chunk_size))
    min_chunked = [min(ch) for ch in chunked]
    return sum(min_chunked, 0.0) / len(min_chunked)

c_size = 20

sims_tc = index_file('timecube_raw.txt')
ave_tc = sum(sims_tc, 0.0) / len(sims_tc)
min_tc = min(sims_tc)
ave_of_mins_tc = ave_of_mins(sims_tc, c_size)
norm_ave_tc = (ave_tc - min_tc) / (max(sims_tc) - min_tc)

sims_ctl = index_file('control_raw.txt')
ave_ctl = sum(sims_ctl, 0.0) / len(sims_ctl)
min_ctl = min(sims_ctl)
ave_of_mins_ctl = ave_of_mins(sims_ctl, c_size)
norm_ave_ctl = (ave_ctl - min_ctl) / (max(sims_ctl) - min_ctl)

print("ave_tc: " + str(ave_tc) + " ave_ctl: " + str(ave_ctl))
print("min_tc: " + str(min_tc) + " min_ctl: " + str(min_ctl))
print("ave_of_mins_tc: " + str(ave_of_mins_tc) + " ave_of_mins_ctl: " + str(ave_of_mins_ctl))
print("norm_ave_tc: " + str(norm_ave_tc) + " norm_ave_ctl: " + str(norm_ave_ctl))

index_string("""
In 1884,  meridian time personnel met
 in Washington to change Earth time.
 In 1884,  meridian time personnel met
 in Washington to change Earth time.
First words said was that only 1 day
could be used on Earth to not change
 the 1 day bible. So they applied the 1
day  and  ignored  the  other  3 days.
The bible time was wrong then and it
 proved wrong today. This a major lie
  has so much evil feed from it's wrong.
No man on Earth has no belly-button,
  it proves every believer on Earth a liar.
""")
