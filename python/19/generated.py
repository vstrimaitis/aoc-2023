import dataclasses
from models import Range, PartRatings

def wkfl_dc(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2420:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2419)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2420), part_ratings.m.r))

    return ans

def wkfl_jb(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2618:vv
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2619), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2618)))
    ans += wkfl_vv(temp_ratings)

    return ans

def wkfl_vxv(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2362:tsk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2363), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2362)))
    ans += wkfl_tsk(temp_ratings)
    
    # m>1949:hpf
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1950), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1949)))
    ans += wkfl_hpf(temp_ratings)
    
    ans += wkfl_qdx(part_ratings)

    return ans

def wkfl_xs(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2562:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2563), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2562)))
    
    # a>2291:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2292), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2291)))
    
    # s<3703:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3702)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3703), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_tl(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1583:hb
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1582)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1583), part_ratings.x.r))
    ans += wkfl_hb(temp_ratings)
    
    ans += wkfl_nd(part_ratings)

    return ans

def wkfl_xk(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3191:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3190)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3191), part_ratings.m.r))
    
    # a>844:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 845), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 844)))
    
    # a<714:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 713)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 714), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_sxh(part_ratings: PartRatings) -> int:
    ans = 0

    # m>128:trk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 129), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 128)))
    ans += wkfl_trk(temp_ratings)
    
    # a<521:qvc
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 520)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 521), part_ratings.a.r))
    ans += wkfl_qvc(temp_ratings)
    
    ans += wkfl_zq(part_ratings)

    return ans

def wkfl_cxv(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1082:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1083), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1082)))
    ans += temp_ratings.total
    
    # s<1006:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1005)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1006), part_ratings.s.r))

    return ans

def wkfl_jsm(part_ratings: PartRatings) -> int:
    ans = 0

    # a>776:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 777), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 776)))
    ans += temp_ratings.total
    
    # m<2436:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2435)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2436), part_ratings.m.r))
    
    ans += part_ratings.total

    return ans

def wkfl_sn(part_ratings: PartRatings) -> int:
    ans = 0

    # a<295:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 294)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 295), part_ratings.a.r))
    ans += temp_ratings.total
    
    # x<1774:fpm
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1773)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1774), part_ratings.x.r))
    ans += wkfl_fpm(temp_ratings)
    
    ans += wkfl_fsk(part_ratings)

    return ans

def wkfl_lld(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2279:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2278)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2279), part_ratings.m.r))
    ans += temp_ratings.total

    return ans

def wkfl_ng(part_ratings: PartRatings) -> int:
    ans = 0

    # a<590:sdl
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 589)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 590), part_ratings.a.r))
    ans += wkfl_sdl(temp_ratings)
    
    # a>609:snx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 610), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 609)))
    ans += wkfl_snx(temp_ratings)

    return ans

def wkfl_sdl(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1719:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1718)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1719), part_ratings.s.r))
    ans += temp_ratings.total
    
    # a<553:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 552)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 553), part_ratings.a.r))
    ans += temp_ratings.total
    
    # s>1738:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1739), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1738)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_hrd(part_ratings: PartRatings) -> int:
    ans = 0

    # s>3215:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3216), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3215)))
    ans += temp_ratings.total
    
    # a>691:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 692), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 691)))
    ans += temp_ratings.total
    
    # m>2571:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2572), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2571)))

    return ans

def wkfl_jq(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2384:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2383)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2384), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s<2587:zlc
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2586)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2587), part_ratings.s.r))
    ans += wkfl_zlc(temp_ratings)
    
    ans += wkfl_txr(part_ratings)

    return ans

def wkfl_gp(part_ratings: PartRatings) -> int:
    ans = 0

    # x>3310:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3311), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3310)))
    
    # s<3337:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3336)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3337), part_ratings.s.r))

    return ans

def wkfl_nk(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3026:jbp
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3025)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3026), part_ratings.a.r))
    ans += wkfl_jbp(temp_ratings)
    
    ans += wkfl_sm(part_ratings)

    return ans

def wkfl_kth(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2224:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2225), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2224)))
    ans += temp_ratings.total

    return ans

def wkfl_plr(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1171:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1170)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1171), part_ratings.x.r))
    ans += temp_ratings.total
    
    # x>1291:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1292), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1291)))
    ans += temp_ratings.total

    return ans

def wkfl_mzl(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2788:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2789), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2788)))

    return ans

def wkfl_clc(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2151:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2152), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2151)))
    
    # a<1437:mr
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1436)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1437), part_ratings.a.r))
    ans += wkfl_mr(temp_ratings)
    
    # s>1993:gj
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1994), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1993)))
    ans += wkfl_gj(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_tzk(part_ratings: PartRatings) -> int:
    ans = 0

    # x<3188:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3187)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3188), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_df(part_ratings: PartRatings) -> int:
    ans = 0

    # s<127:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 126)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 127), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_cjz(part_ratings: PartRatings) -> int:
    ans = 0

    # x<551:rr
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 550)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 551), part_ratings.x.r))
    ans += wkfl_rr(temp_ratings)
    
    # a<3279:kpg
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3278)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3279), part_ratings.a.r))
    ans += wkfl_kpg(temp_ratings)
    
    # m<3044:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3043)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3044), part_ratings.m.r))

    return ans

def wkfl_zpn(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1044:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1043)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1044), part_ratings.s.r))
    
    # a<928:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 927)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 928), part_ratings.a.r))
    
    # x>667:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 668), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 667)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_qlq(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3396:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3395)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3396), part_ratings.a.r))
    ans += temp_ratings.total
    
    # m<188:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 187)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 188), part_ratings.m.r))
    ans += temp_ratings.total

    return ans

def wkfl_xl(part_ratings: PartRatings) -> int:
    ans = 0

    # x>871:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 872), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 871)))
    
    # x<576:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 575)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 576), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += wkfl_fls(part_ratings)

    return ans

def wkfl_hrj(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1772:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1771)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1772), part_ratings.x.r))
    ans += temp_ratings.total
    
    # x<2715:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2714)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2715), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_kb(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1475:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1476), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1475)))
    
    # m<3188:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3187)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3188), part_ratings.m.r))

    return ans

def wkfl_ljt(part_ratings: PartRatings) -> int:
    ans = 0

    # x<3132:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3131)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3132), part_ratings.x.r))
    
    # s<1543:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1542)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1543), part_ratings.s.r))
    
    # s>1572:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1573), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1572)))
    
    ans += part_ratings.total

    return ans

def wkfl_fl(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2964:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2965), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2964)))
    
    # x<2878:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2877)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2878), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_pn(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1842:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1843), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1842)))
    
    # a<1709:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1708)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1709), part_ratings.a.r))
    
    # x<2041:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2040)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2041), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_tfn(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2189:ntn
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2188)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2189), part_ratings.s.r))
    ans += wkfl_ntn(temp_ratings)
    
    # x<2729:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2728)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2729), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_vlb(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2382:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2383), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2382)))

    return ans

def wkfl_njr(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1634:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1633)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1634), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_fh(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2659:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2660), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2659)))
    
    # s<3385:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3384)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3385), part_ratings.s.r))
    
    # m<3515:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3514)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3515), part_ratings.m.r))
    ans += temp_ratings.total

    return ans

def wkfl_lbl(part_ratings: PartRatings) -> int:
    ans = 0

    # a>532:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 533), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 532)))
    
    ans += part_ratings.total

    return ans

def wkfl_pt(part_ratings: PartRatings) -> int:
    ans = 0

    # x>684:nm
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 685), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 684)))
    ans += wkfl_nm(temp_ratings)
    
    ans += wkfl_pgc(part_ratings)

    return ans

def wkfl_dq(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2740:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2741), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2740)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_ldb(part_ratings: PartRatings) -> int:
    ans = 0

    # m<54:zj
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 53)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 54), part_ratings.m.r))
    ans += wkfl_zj(temp_ratings)
    
    # a>1147:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1148), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1147)))
    
    ans += part_ratings.total

    return ans

def wkfl_lxm(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1904:ms
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1903)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1904), part_ratings.x.r))
    ans += wkfl_ms(temp_ratings)
    
    # x<1973:ptx
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1972)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1973), part_ratings.x.r))
    ans += wkfl_ptx(temp_ratings)
    
    # s<1616:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1615)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1616), part_ratings.s.r))
    
    ans += wkfl_nms(part_ratings)

    return ans

def wkfl_xgl(part_ratings: PartRatings) -> int:
    ans = 0

    # x<732:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 731)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 732), part_ratings.x.r))
    
    # m>3339:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3340), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3339)))
    ans += temp_ratings.total
    
    # a>289:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 290), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 289)))
    
    ans += part_ratings.total

    return ans

def wkfl_crj(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1193:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1194), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1193)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_mf(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2400:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2401), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2400)))
    ans += temp_ratings.total
    
    # s>570:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 571), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 570)))
    ans += temp_ratings.total

    return ans

def wkfl_pfn(part_ratings: PartRatings) -> int:
    ans = 0

    # a>55:lfz
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 56), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 55)))
    ans += wkfl_lfz(temp_ratings)
    
    ans += wkfl_pdt(part_ratings)

    return ans

def wkfl_gdc(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1141:hsq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1142), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1141)))
    ans += wkfl_hsq(temp_ratings)
    
    # x>1870:dd
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1871), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1870)))
    ans += wkfl_dd(temp_ratings)
    
    # a>1080:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1081), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1080)))
    ans += temp_ratings.total
    
    ans += wkfl_prn(part_ratings)

    return ans

def wkfl_snx(part_ratings: PartRatings) -> int:
    ans = 0

    # a<629:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 628)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 629), part_ratings.a.r))
    
    ans += part_ratings.total

    return ans

def wkfl_kgc(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1534:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1533)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1534), part_ratings.m.r))
    ans += temp_ratings.total
    
    # x>3548:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3549), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3548)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_sj(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1933:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1934), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1933)))
    ans += temp_ratings.total
    
    ans += wkfl_lx(part_ratings)

    return ans

def wkfl_cz(part_ratings: PartRatings) -> int:
    ans = 0

    # a>837:xqq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 838), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 837)))
    ans += wkfl_xqq(temp_ratings)
    
    # s>1030:lb
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1031), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1030)))
    ans += wkfl_lb(temp_ratings)
    
    ans += wkfl_hzs(part_ratings)

    return ans

def wkfl_rsf(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2637:bjr
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2638), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2637)))
    ans += wkfl_bjr(temp_ratings)
    
    # a>1525:bk
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1526), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1525)))
    ans += wkfl_bk(temp_ratings)
    
    # m<2492:hl
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2491)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2492), part_ratings.m.r))
    ans += wkfl_hl(temp_ratings)
    
    ans += wkfl_xj(part_ratings)

    return ans

def wkfl_ckd(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3384:mcs
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3383)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3384), part_ratings.m.r))
    ans += wkfl_mcs(temp_ratings)
    
    # a<2487:nv
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2486)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2487), part_ratings.a.r))
    ans += wkfl_nv(temp_ratings)
    
    # m<3630:gtd
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3629)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3630), part_ratings.m.r))
    ans += wkfl_gtd(temp_ratings)
    
    ans += wkfl_jq(part_ratings)

    return ans

def wkfl_gr(part_ratings: PartRatings) -> int:
    ans = 0

    # m<941:srr
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 940)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 941), part_ratings.m.r))
    ans += wkfl_srr(temp_ratings)
    
    # s<3207:fq
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3206)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3207), part_ratings.s.r))
    ans += wkfl_fq(temp_ratings)
    
    # a>563:gc
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 564), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 563)))
    ans += wkfl_gc(temp_ratings)
    
    ans += wkfl_rt(part_ratings)

    return ans

def wkfl_brt(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2243:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2244), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2243)))
    
    ans += part_ratings.total

    return ans

def wkfl_cvk(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2740:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2739)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2740), part_ratings.x.r))
    
    # s>1596:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1597), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1596)))
    
    # a>789:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 790), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 789)))
    ans += temp_ratings.total

    return ans

def wkfl_fg(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1050:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1049)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1050), part_ratings.m.r))
    ans += temp_ratings.total

    return ans

def wkfl_sm(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3394:pj
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3395), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3394)))
    ans += wkfl_pj(temp_ratings)
    
    ans += wkfl_phh(part_ratings)

    return ans

def wkfl_ktc(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2073:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2072)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2073), part_ratings.x.r))
    
    ans += wkfl_cvk(part_ratings)

    return ans

def wkfl_sqq(part_ratings: PartRatings) -> int:
    ans = 0

    # s<373:bst
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 372)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 373), part_ratings.s.r))
    ans += wkfl_bst(temp_ratings)
    
    # a>509:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 510), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 509)))
    ans += temp_ratings.total
    
    # m<1387:crh
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1386)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1387), part_ratings.m.r))
    ans += wkfl_crh(temp_ratings)

    return ans

def wkfl_rqp(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2332:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2333), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2332)))
    
    # x<2127:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2126)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2127), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_cpp(part_ratings: PartRatings) -> int:
    ans = 0

    # s>365:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 366), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 365)))
    
    # m<451:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 450)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 451), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s<226:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 225)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 226), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_ds(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2018:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2017)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2018), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s>1329:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1330), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1329)))
    ans += temp_ratings.total

    return ans

def wkfl_qc(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2041:dj
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2042), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2041)))
    ans += wkfl_dj(temp_ratings)
    
    ans += wkfl_tbx(part_ratings)

    return ans

def wkfl_cdh(part_ratings: PartRatings) -> int:
    ans = 0

    # a>932:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 933), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 932)))
    
    ans += part_ratings.total

    return ans

def wkfl_tsk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<694:pqq
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 693)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 694), part_ratings.s.r))
    ans += wkfl_pqq(temp_ratings)
    
    # s>1274:rth
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1275), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1274)))
    ans += wkfl_rth(temp_ratings)
    
    ans += wkfl_sh(part_ratings)

    return ans

def wkfl_hns(part_ratings: PartRatings) -> int:
    ans = 0

    # a<507:fx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 506)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 507), part_ratings.a.r))
    ans += wkfl_fx(temp_ratings)
    
    # x<885:fxz
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 884)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 885), part_ratings.x.r))
    ans += wkfl_fxz(temp_ratings)
    
    # s<1679:nxj
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1678)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1679), part_ratings.s.r))
    ans += wkfl_nxj(temp_ratings)
    
    ans += wkfl_jjm(part_ratings)

    return ans

def wkfl_prn(part_ratings: PartRatings) -> int:
    ans = 0

    # m<150:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 149)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 150), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s<3241:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3240)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3241), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_cn(part_ratings: PartRatings) -> int:
    ans = 0

    # x<728:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 727)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 728), part_ratings.x.r))
    ans += temp_ratings.total
    
    # a>515:mzl
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 516), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 515)))
    ans += wkfl_mzl(temp_ratings)
    
    # x>1222:cbx
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1223), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1222)))
    ans += wkfl_cbx(temp_ratings)

    return ans

def wkfl_jxh(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1038:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1039), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1038)))
    
    # s>1571:rs
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1572), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1571)))
    ans += wkfl_rs(temp_ratings)
    
    # a<899:rxp
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 898)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 899), part_ratings.a.r))
    ans += wkfl_rxp(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_nd(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1206:rp
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1207), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1206)))
    ans += wkfl_rp(temp_ratings)
    
    # x>3028:rvm
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3029), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3028)))
    ans += wkfl_rvm(temp_ratings)
    
    # a<1090:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1089)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1090), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += wkfl_hh(part_ratings)

    return ans

def wkfl_thg(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1565:tnf
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1564)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1565), part_ratings.a.r))
    ans += wkfl_tnf(temp_ratings)
    
    # x<1487:cx
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1486)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1487), part_ratings.x.r))
    ans += wkfl_cx(temp_ratings)
    
    # s>3604:mk
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3605), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3604)))
    ans += wkfl_mk(temp_ratings)
    
    ans += wkfl_lkj(part_ratings)

    return ans

def wkfl_fzf(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2657:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2658), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2657)))
    
    # s<1584:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1583)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1584), part_ratings.s.r))
    ans += temp_ratings.total
    
    # m<413:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 412)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 413), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += wkfl_xjb(part_ratings)

    return ans

def wkfl_xcd(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2376:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2375)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2376), part_ratings.a.r))
    ans += temp_ratings.total
    
    # x<1682:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1681)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1682), part_ratings.x.r))

    return ans

def wkfl_qnd(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3633:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3634), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3633)))
    ans += temp_ratings.total
    
    # m>3408:tks
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3409), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3408)))
    ans += wkfl_tks(temp_ratings)
    
    # s>872:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 873), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 872)))
    
    ans += part_ratings.total

    return ans

def wkfl_sbz(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1838:gs
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1839), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1838)))
    ans += wkfl_gs(temp_ratings)
    
    # x<1590:dft
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1589)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1590), part_ratings.x.r))
    ans += wkfl_dft(temp_ratings)
    
    # x>3011:xmq
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3012), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3011)))
    ans += wkfl_xmq(temp_ratings)
    
    ans += wkfl_zms(part_ratings)

    return ans

def wkfl_zch(part_ratings: PartRatings) -> int:
    ans = 0

    # s>194:bx
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 195), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 194)))
    ans += wkfl_bx(temp_ratings)

    return ans

def wkfl_zcq(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2460:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2461), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2460)))
    
    # s<1436:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1435)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1436), part_ratings.s.r))
    ans += temp_ratings.total
    
    # m>2291:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2292), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2291)))
    
    ans += wkfl_brt(part_ratings)

    return ans

def wkfl_txr(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2774:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2773)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2774), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s<2873:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2872)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2873), part_ratings.s.r))
    
    # a<3258:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3257)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3258), part_ratings.a.r))

    return ans

def wkfl_fls(part_ratings: PartRatings) -> int:
    ans = 0

    # x>747:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 748), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 747)))
    ans += temp_ratings.total

    return ans

def wkfl_dp(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2534:jzq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2533)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2534), part_ratings.a.r))
    ans += wkfl_jzq(temp_ratings)
    
    ans += wkfl_cpt(part_ratings)

    return ans

def wkfl_cs(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1593:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1592)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1593), part_ratings.a.r))
    
    # x<2725:pn
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2724)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2725), part_ratings.x.r))
    ans += wkfl_pn(temp_ratings)
    
    # x<3189:dfq
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3188)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3189), part_ratings.x.r))
    ans += wkfl_dfq(temp_ratings)

    return ans

def wkfl_pgs(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2514:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2515), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2514)))
    ans += temp_ratings.total
    
    # a<973:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 972)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 973), part_ratings.a.r))
    
    # s<1278:xh
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1277)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1278), part_ratings.s.r))
    ans += wkfl_xh(temp_ratings)
    
    ans += wkfl_vs(part_ratings)

    return ans

def wkfl_mxc(part_ratings: PartRatings) -> int:
    ans = 0

    # a>330:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 331), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 330)))
    ans += temp_ratings.total
    
    # s<3406:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3405)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3406), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_grb(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3474:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3473)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3474), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_zzc(part_ratings: PartRatings) -> int:
    ans = 0

    # x<3201:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3200)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3201), part_ratings.x.r))
    ans += temp_ratings.total
    
    # m>1081:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1082), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1081)))
    
    ans += part_ratings.total

    return ans

def wkfl_rxp(part_ratings: PartRatings) -> int:
    ans = 0

    # m>887:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 888), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 887)))
    
    # s<1496:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1495)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1496), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_zbz(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2646:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2647), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2646)))
    ans += temp_ratings.total
    
    # m>2836:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2837), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2836)))
    ans += temp_ratings.total

    return ans

def wkfl_jvp(part_ratings: PartRatings) -> int:
    ans = 0

    # a>585:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 586), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 585)))
    ans += temp_ratings.total

    return ans

def wkfl_nqf(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1568:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1569), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1568)))
    ans += temp_ratings.total

    return ans

def wkfl_xr(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1713:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1714), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1713)))
    ans += temp_ratings.total
    
    # a>426:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 427), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 426)))
    ans += temp_ratings.total

    return ans

def wkfl_qjx(part_ratings: PartRatings) -> int:
    ans = 0

    # m<270:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 269)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 270), part_ratings.m.r))
    
    # m>538:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 539), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 538)))
    ans += temp_ratings.total
    
    ans += wkfl_tf(part_ratings)

    return ans

def wkfl_rck(part_ratings: PartRatings) -> int:
    ans = 0

    # m<265:vmt
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 264)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 265), part_ratings.m.r))
    ans += wkfl_vmt(temp_ratings)
    
    # a<3724:xmz
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3723)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3724), part_ratings.a.r))
    ans += wkfl_xmz(temp_ratings)
    
    ans += wkfl_vzt(part_ratings)

    return ans

def wkfl_bvg(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2924:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2925), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2924)))
    
    # s>848:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 849), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 848)))
    ans += temp_ratings.total
    
    # a<555:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 554)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 555), part_ratings.a.r))

    return ans

def wkfl_qhv(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1761:ccx
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1762), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1761)))
    ans += wkfl_ccx(temp_ratings)
    
    ans += wkfl_pts(part_ratings)

    return ans

def wkfl_xc(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1159:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1158)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1159), part_ratings.a.r))
    ans += temp_ratings.total
    
    # x<1697:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1696)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1697), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_sdj(part_ratings: PartRatings) -> int:
    ans = 0

    # m>314:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 315), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 314)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_lxc(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1534:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1535), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1534)))
    ans += temp_ratings.total
    
    # s>3403:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3404), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3403)))
    ans += temp_ratings.total
    
    # a>865:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 866), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 865)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_pgj(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1955:hhp
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1956), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1955)))
    ans += wkfl_hhp(temp_ratings)
    
    # a>2764:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2765), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2764)))
    
    # x<1140:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1139)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1140), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += wkfl_xzp(part_ratings)

    return ans

def wkfl_qcr(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1970:xpf
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1971), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1970)))
    ans += wkfl_xpf(temp_ratings)
    
    # a<1081:gr
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1080)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1081), part_ratings.a.r))
    ans += wkfl_gr(temp_ratings)
    
    # x<981:mdc
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 980)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 981), part_ratings.x.r))
    ans += wkfl_mdc(temp_ratings)
    
    ans += wkfl_qjm(part_ratings)

    return ans

def wkfl_gj(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2096:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2097), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2096)))
    ans += temp_ratings.total
    
    # s<2044:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2043)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2044), part_ratings.s.r))

    return ans

def wkfl_jmf(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1086:tn
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1087), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1086)))
    ans += wkfl_tn(temp_ratings)
    
    # s>891:jfc
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 892), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 891)))
    ans += wkfl_jfc(temp_ratings)

    return ans

def wkfl_pq(part_ratings: PartRatings) -> int:
    ans = 0

    # a>933:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 934), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 933)))
    ans += temp_ratings.total
    
    # m>1455:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1456), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1455)))
    
    # x<3710:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3709)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3710), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_kkl(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1161:brd
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1160)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1161), part_ratings.s.r))
    ans += wkfl_brd(temp_ratings)
    
    ans += wkfl_tjz(part_ratings)

    return ans

def wkfl_gvn(part_ratings: PartRatings) -> int:
    ans = 0

    # m<368:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 367)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 368), part_ratings.m.r))
    
    # m<499:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 498)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 499), part_ratings.m.r))
    
    ans += part_ratings.total

    return ans

def wkfl_mh(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3341:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3340)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3341), part_ratings.m.r))
    ans += temp_ratings.total
    
    # m<3772:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3771)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3772), part_ratings.m.r))
    ans += temp_ratings.total
    
    # x>961:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 962), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 961)))
    
    ans += part_ratings.total

    return ans

def wkfl_fxz(part_ratings: PartRatings) -> int:
    ans = 0

    # x<313:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 312)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 313), part_ratings.x.r))

    return ans

def wkfl_mz(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1635:cn
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1636), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1635)))
    ans += wkfl_cn(temp_ratings)
    
    # m<881:hns
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 880)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 881), part_ratings.m.r))
    ans += wkfl_hns(temp_ratings)
    
    ans += wkfl_clg(part_ratings)

    return ans

def wkfl_brd(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1514:hm
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1515), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1514)))
    ans += wkfl_hm(temp_ratings)
    
    # m>2103:xsm
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2104), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2103)))
    ans += wkfl_xsm(temp_ratings)
    
    ans += wkfl_lsf(part_ratings)

    return ans

def wkfl_hvl(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3884:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3883)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3884), part_ratings.m.r))
    
    # m<3891:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3890)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3891), part_ratings.m.r))
    
    ans += part_ratings.total

    return ans

def wkfl_tp(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2386:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2385)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2386), part_ratings.s.r))
    ans += temp_ratings.total
    
    # m<1033:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1032)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1033), part_ratings.m.r))
    
    # a<657:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 656)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 657), part_ratings.a.r))

    return ans

def wkfl_hb(part_ratings: PartRatings) -> int:
    ans = 0

    # m<97:pf
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 96)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 97), part_ratings.m.r))
    ans += wkfl_pf(temp_ratings)
    
    # s>2312:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2313), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2312)))

    return ans

def wkfl_vrm(part_ratings: PartRatings) -> int:
    ans = 0

    # s<901:cpp
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 900)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 901), part_ratings.s.r))
    ans += wkfl_cpp(temp_ratings)
    
    # s>1305:hhr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1306), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1305)))
    ans += wkfl_hhr(temp_ratings)
    
    # a<146:cnq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 145)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 146), part_ratings.a.r))
    ans += wkfl_cnq(temp_ratings)
    
    ans += wkfl_dgf(part_ratings)

    return ans

def wkfl_vc(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1191:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1190)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1191), part_ratings.a.r))
    ans += temp_ratings.total
    
    # m>728:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 729), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 728)))
    ans += temp_ratings.total

    return ans

def wkfl_tf(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3424:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3425), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3424)))
    ans += temp_ratings.total
    
    # a<3301:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3300)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3301), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_vhb(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1274:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1273)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1274), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_xcs(part_ratings: PartRatings) -> int:
    ans = 0

    # a<871:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 870)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 871), part_ratings.a.r))
    
    # a<1588:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1587)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1588), part_ratings.a.r))

    return ans

def wkfl_dh(part_ratings: PartRatings) -> int:
    ans = 0

    # x<601:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 600)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 601), part_ratings.x.r))
    
    # a<351:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 350)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 351), part_ratings.a.r))
    ans += temp_ratings.total
    
    # x>872:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 873), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 872)))
    ans += temp_ratings.total

    return ans

def wkfl_gxr(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3357:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3358), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3357)))
    ans += temp_ratings.total
    
    # a<3143:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3142)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3143), part_ratings.a.r))
    
    ans += part_ratings.total

    return ans

def wkfl_mgk(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3299:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3300), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3299)))
    
    # m<45:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 44)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 45), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_xtz(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1471:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1472), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1471)))
    ans += temp_ratings.total
    
    # m>1107:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1108), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1107)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_dr(part_ratings: PartRatings) -> int:
    ans = 0

    # s>441:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 442), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 441)))
    ans += temp_ratings.total
    
    # a>3261:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3262), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3261)))
    ans += temp_ratings.total
    
    # a>3216:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3217), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3216)))
    ans += temp_ratings.total

    return ans

def wkfl_srs(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1069:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1068)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1069), part_ratings.s.r))
    
    # s<1099:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1098)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1099), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_qjm(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2827:clc
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2826)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2827), part_ratings.s.r))
    ans += wkfl_clc(temp_ratings)
    
    ans += wkfl_thg(part_ratings)

    return ans

def wkfl_tkq(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1882:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1883), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1882)))
    ans += temp_ratings.total
    
    # x<3265:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3264)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3265), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_xsm(part_ratings: PartRatings) -> int:
    ans = 0

    # s<759:srg
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 758)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 759), part_ratings.s.r))
    ans += wkfl_srg(temp_ratings)
    
    # m<3323:dn
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3322)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3323), part_ratings.m.r))
    ans += wkfl_dn(temp_ratings)
    
    # s<937:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 936)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 937), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += wkfl_cxv(part_ratings)

    return ans

def wkfl_nxj(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1661:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1660)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1661), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s<1668:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1667)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1668), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_xsk(part_ratings: PartRatings) -> int:
    ans = 0

    # a>19:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 20), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 19)))
    ans += temp_ratings.total
    
    # s>3781:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3782), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3781)))

    return ans

def wkfl_qlg(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2587:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2586)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2587), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_jft(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2232:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2231)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2232), part_ratings.x.r))
    
    # x>2411:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2412), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2411)))

    return ans

def wkfl_dx(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2552:jdj
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2551)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2552), part_ratings.x.r))
    ans += wkfl_jdj(temp_ratings)
    
    # x>3346:jvg
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3347), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3346)))
    ans += wkfl_jvg(temp_ratings)
    
    ans += wkfl_xsx(part_ratings)

    return ans

def wkfl_zr(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2400:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2399)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2400), part_ratings.x.r))
    ans += temp_ratings.total
    
    # m<3690:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3689)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3690), part_ratings.m.r))
    
    # x>2593:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2594), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2593)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_rn(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2915:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2914)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2915), part_ratings.m.r))
    
    # m>3162:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3163), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3162)))
    ans += temp_ratings.total

    return ans

def wkfl_cqh(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1070:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1069)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1070), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_kn(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1557:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1556)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1557), part_ratings.x.r))
    ans += temp_ratings.total
    
    # s>2799:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2800), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2799)))
    ans += temp_ratings.total
    
    ans += wkfl_mvm(part_ratings)

    return ans

def wkfl_pnp(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2753:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2752)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2753), part_ratings.a.r))
    
    # x>2405:fh
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2406), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2405)))
    ans += wkfl_fh(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_lrf(part_ratings: PartRatings) -> int:
    ans = 0

    # m<335:rk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 334)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 335), part_ratings.m.r))
    ans += wkfl_rk(temp_ratings)
    
    # a>3635:zch
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3636), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3635)))
    ans += wkfl_zch(temp_ratings)
    
    ans += wkfl_gg(part_ratings)

    return ans

def wkfl_zv(part_ratings: PartRatings) -> int:
    ans = 0

    # s<663:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 662)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 663), part_ratings.s.r))
    
    # x>3288:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3289), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3288)))
    
    ans += part_ratings.total

    return ans

def wkfl_nxr(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2407:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2406)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2407), part_ratings.x.r))
    
    # a>359:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 360), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 359)))

    return ans

def wkfl_ntn(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2865:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2864)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2865), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_zjg(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1922:zbh
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1923), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1922)))
    ans += wkfl_zbh(temp_ratings)
    
    # m<2586:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2585)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2586), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += wkfl_cq(part_ratings)

    return ans

def wkfl_jx(part_ratings: PartRatings) -> int:
    ans = 0

    # s<792:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 791)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 792), part_ratings.s.r))
    
    # x>2184:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2185), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2184)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_xmq(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1660:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1659)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1660), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += wkfl_vt(part_ratings)

    return ans

def wkfl_mm(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1841:mgz
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1840)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1841), part_ratings.a.r))
    ans += wkfl_mgz(temp_ratings)
    
    # a>1953:mv
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1954), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1953)))
    ans += wkfl_mv(temp_ratings)
    
    # x>2296:tzk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2297), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2296)))
    ans += wkfl_tzk(temp_ratings)
    
    ans += wkfl_fzb(part_ratings)

    return ans

def wkfl_rth(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3397:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3398), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3397)))
    
    ans += wkfl_tj(part_ratings)

    return ans

def wkfl_jbt(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3554:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3553)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3554), part_ratings.a.r))
    ans += temp_ratings.total
    
    # s<413:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 412)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 413), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_bk(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2506:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2507), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2506)))
    
    # s>2288:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2289), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2288)))
    
    # a<2022:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2021)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2022), part_ratings.a.r))
    
    ans += part_ratings.total

    return ans

def wkfl_qtg(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3189:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3190), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3189)))
    ans += temp_ratings.total
    
    # m<2647:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2646)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2647), part_ratings.m.r))
    
    # s<1098:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1097)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1098), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_bpr(part_ratings: PartRatings) -> int:
    ans = 0

    # x<3352:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3351)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3352), part_ratings.x.r))
    ans += temp_ratings.total
    
    # x>3720:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3721), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3720)))
    ans += temp_ratings.total

    return ans

def wkfl_hqs(part_ratings: PartRatings) -> int:
    ans = 0

    # a>941:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 942), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 941)))
    
    # x>530:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 531), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 530)))
    ans += temp_ratings.total
    
    # x<253:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 252)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 253), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_chg(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2676:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2675)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2676), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_cnl(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3057:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3056)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3057), part_ratings.m.r))
    
    ans += wkfl_qnt(part_ratings)

    return ans

def wkfl_rvm(part_ratings: PartRatings) -> int:
    ans = 0

    # x>3655:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3656), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3655)))
    
    # s>2266:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2267), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2266)))
    ans += temp_ratings.total
    
    # m<90:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 89)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 90), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_znc(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1897:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1896)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1897), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_xsx(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2921:srs
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2920)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2921), part_ratings.x.r))
    ans += wkfl_srs(temp_ratings)
    
    # x>3066:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3067), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3066)))
    ans += temp_ratings.total
    
    # a<842:vcf
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 841)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 842), part_ratings.a.r))
    ans += wkfl_vcf(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_vsz(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3368:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3367)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3368), part_ratings.m.r))
    
    # x<1768:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1767)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1768), part_ratings.x.r))
    ans += temp_ratings.total
    
    # s<1653:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1652)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1653), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_mrh(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1352:kth
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1353), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1352)))
    ans += wkfl_kth(temp_ratings)
    
    # s>2546:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2547), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2546)))
    
    # s>2154:vlb
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2155), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2154)))
    ans += wkfl_vlb(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_jvg(part_ratings: PartRatings) -> int:
    ans = 0

    # a<863:kgp
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 862)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 863), part_ratings.a.r))
    ans += wkfl_kgp(temp_ratings)
    
    # s>1043:nbm
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1044), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1043)))
    ans += wkfl_nbm(temp_ratings)
    
    # a<999:pq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 998)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 999), part_ratings.a.r))
    ans += wkfl_pq(temp_ratings)
    
    ans += wkfl_gsr(part_ratings)

    return ans

def wkfl_rdk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<573:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 572)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 573), part_ratings.s.r))
    ans += temp_ratings.total
    
    # x<315:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 314)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 315), part_ratings.x.r))

    return ans

def wkfl_tb(part_ratings: PartRatings) -> int:
    ans = 0

    # x>522:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 523), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 522)))
    
    # x<332:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 331)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 332), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_kkr(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1675:dqp
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1674)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1675), part_ratings.m.r))
    ans += wkfl_dqp(temp_ratings)

    return ans

def wkfl_lkj(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1662:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1663), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1662)))
    
    # m>1068:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1069), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1068)))
    ans += temp_ratings.total

    return ans

def wkfl_jn(part_ratings: PartRatings) -> int:
    ans = 0

    # m<46:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 45)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 46), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s<3886:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3885)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3886), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_cvn(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1734:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1735), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1734)))
    
    ans += part_ratings.total

    return ans

def wkfl_crr(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3221:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3222), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3221)))
    ans += temp_ratings.total
    
    # a<3093:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3092)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3093), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_ggm(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3699:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3700), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3699)))
    
    # m<3433:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3432)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3433), part_ratings.m.r))
    
    ans += part_ratings.total

    return ans

def wkfl_nl(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1368:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1369), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1368)))
    
    ans += part_ratings.total

    return ans

def wkfl_qpn(part_ratings: PartRatings) -> int:
    ans = 0

    # m>623:jxh
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 624), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 623)))
    ans += wkfl_jxh(temp_ratings)
    
    ans += wkfl_blb(part_ratings)

    return ans

def wkfl_mgz(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1545:hct
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1546), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1545)))
    ans += wkfl_hct(temp_ratings)
    
    # m<99:kvg
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 98)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 99), part_ratings.m.r))
    ans += wkfl_kvg(temp_ratings)
    
    # m<166:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 165)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 166), part_ratings.m.r))
    
    ans += wkfl_cl(part_ratings)

    return ans

def wkfl_jl(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1514:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1515), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1514)))
    ans += temp_ratings.total
    
    # s<2760:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2759)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2760), part_ratings.s.r))

    return ans

def wkfl_jjm(part_ratings: PartRatings) -> int:
    ans = 0

    # a<585:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 584)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 585), part_ratings.a.r))
    
    # m<518:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 517)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 518), part_ratings.m.r))
    ans += temp_ratings.total
    
    # a>621:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 622), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 621)))
    
    ans += part_ratings.total

    return ans

def wkfl_pdt(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1100:zmk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1101), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1100)))
    ans += wkfl_zmk(temp_ratings)
    
    # x>2084:rbk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2085), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2084)))
    ans += wkfl_rbk(temp_ratings)

    return ans

def wkfl_srg(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1251:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1252), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1251)))
    
    # a<1171:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1170)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1171), part_ratings.a.r))
    
    # a>1199:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1200), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1199)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_gz(part_ratings: PartRatings) -> int:
    ans = 0

    # a>942:bsz
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 943), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 942)))
    ans += wkfl_bsz(temp_ratings)
    
    # s>603:fv
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 604), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 603)))
    ans += wkfl_fv(temp_ratings)
    
    # s<513:sqf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 512)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 513), part_ratings.s.r))
    ans += wkfl_sqf(temp_ratings)
    
    ans += wkfl_llh(part_ratings)

    return ans

def wkfl_xn(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2495:xm
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2496), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2495)))
    ans += wkfl_xm(temp_ratings)
    
    # x<886:mb
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 885)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 886), part_ratings.x.r))
    ans += wkfl_mb(temp_ratings)
    
    # s>2560:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2561), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2560)))

    return ans

def wkfl_hnf(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2103:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2102)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2103), part_ratings.m.r))

    return ans

def wkfl_vlx(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1474:vxv
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1475), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1474)))
    ans += wkfl_vxv(temp_ratings)
    
    # s<714:sff
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 713)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 714), part_ratings.s.r))
    ans += wkfl_sff(temp_ratings)
    
    ans += wkfl_cjc(part_ratings)

    return ans

def wkfl_mvm(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3096:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3097), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3096)))
    
    # a<3112:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3111)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3112), part_ratings.a.r))

    return ans

def wkfl_zcd(part_ratings: PartRatings) -> int:
    ans = 0

    # a>336:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 337), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 336)))
    
    # x<2664:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2663)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2664), part_ratings.x.r))

    return ans

def wkfl_ck(part_ratings: PartRatings) -> int:
    ans = 0

    # m<115:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 114)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 115), part_ratings.m.r))
    
    # x<717:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 716)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 717), part_ratings.x.r))

    return ans

def wkfl_ld(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2943:tz
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2944), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2943)))
    ans += wkfl_tz(temp_ratings)
    
    # m<2944:rsf
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2943)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2944), part_ratings.m.r))
    ans += wkfl_rsf(temp_ratings)
    
    ans += wkfl_vl(part_ratings)

    return ans

def wkfl_ndz(part_ratings: PartRatings) -> int:
    ans = 0

    # x<427:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 426)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 427), part_ratings.x.r))
    
    # x<603:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 602)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 603), part_ratings.x.r))
    ans += temp_ratings.total
    
    # s>1486:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1487), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1486)))
    
    ans += part_ratings.total

    return ans

def wkfl_km(part_ratings: PartRatings) -> int:
    ans = 0

    # s<988:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 987)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 988), part_ratings.s.r))
    ans += temp_ratings.total
    
    # x<961:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 960)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 961), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_flk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3049:gvn
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3048)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3049), part_ratings.s.r))
    ans += wkfl_gvn(temp_ratings)

    return ans

def wkfl_hsq(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1234:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1235), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1234)))
    
    # x>2510:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2511), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2510)))
    
    # m<104:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 103)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 104), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_kd(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2938:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2937)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2938), part_ratings.a.r))
    
    # a<3461:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3460)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3461), part_ratings.a.r))
    ans += temp_ratings.total
    
    # s<439:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 438)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 439), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_tc(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2499:bv
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2500), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2499)))
    ans += wkfl_bv(temp_ratings)
    
    # m>325:dxp
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 326), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 325)))
    ans += wkfl_dxp(temp_ratings)
    
    # s>431:mf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 432), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 431)))
    ans += wkfl_mf(temp_ratings)
    
    ans += wkfl_jbm(part_ratings)

    return ans

def wkfl_rrc(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1770:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1771), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1770)))
    
    # s<3008:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3007)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3008), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s>3545:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3546), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3545)))
    
    ans += part_ratings.total

    return ans

def wkfl_tnd(part_ratings: PartRatings) -> int:
    ans = 0

    # s<920:sbl
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 919)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 920), part_ratings.s.r))
    ans += wkfl_sbl(temp_ratings)
    
    # x<946:hdl
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 945)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 946), part_ratings.x.r))
    ans += wkfl_hdl(temp_ratings)
    
    ans += wkfl_frt(part_ratings)

    return ans

def wkfl_zmk(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1592:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1593), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1592)))
    
    # x<2341:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2340)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2341), part_ratings.x.r))
    
    # s>1068:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1069), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1068)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_llh(part_ratings: PartRatings) -> int:
    ans = 0

    # a<841:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 840)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 841), part_ratings.a.r))

    return ans

def wkfl_rd(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1565:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1566), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1565)))
    
    # x>3214:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3215), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3214)))
    
    # s>1519:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1520), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1519)))
    ans += temp_ratings.total

    return ans

def wkfl_rmq(part_ratings: PartRatings) -> int:
    ans = 0

    # a<898:ftx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 897)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 898), part_ratings.a.r))
    ans += wkfl_ftx(temp_ratings)
    
    # x>3382:cbp
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3383), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3382)))
    ans += wkfl_cbp(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_sbh(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1905:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1904)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1905), part_ratings.m.r))
    
    # s>3213:ql
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3214), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3213)))
    ans += wkfl_ql(temp_ratings)
    
    # m<2126:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2125)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2126), part_ratings.m.r))

    return ans

def wkfl_tqf(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1553:flk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1552)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1553), part_ratings.x.r))
    ans += wkfl_flk(temp_ratings)
    
    # m<358:khz
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 357)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 358), part_ratings.m.r))
    ans += wkfl_khz(temp_ratings)
    
    # m<465:jl
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 464)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 465), part_ratings.m.r))
    ans += wkfl_jl(temp_ratings)
    
    ans += wkfl_cs(part_ratings)

    return ans

def wkfl_tlp(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3575:qjx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3574)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3575), part_ratings.a.r))
    ans += wkfl_qjx(temp_ratings)
    
    # x<1564:rck
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1563)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1564), part_ratings.x.r))
    ans += wkfl_rck(temp_ratings)
    
    ans += wkfl_cg(part_ratings)

    return ans

def wkfl_xz(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2317:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2318), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2317)))
    
    # a<3490:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3489)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3490), part_ratings.a.r))
    
    # x>2510:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2511), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2510)))
    ans += temp_ratings.total

    return ans

def wkfl_vm(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2836:jg
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2835)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2836), part_ratings.a.r))
    ans += wkfl_jg(temp_ratings)
    
    # m<1749:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1748)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1749), part_ratings.m.r))
    ans += temp_ratings.total

    return ans

def wkfl_mv(part_ratings: PartRatings) -> int:
    ans = 0

    # m>105:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 106), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 105)))
    
    # s<2958:tsq
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2957)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2958), part_ratings.s.r))
    ans += wkfl_tsq(temp_ratings)
    
    # s>3568:nqf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3569), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3568)))
    ans += wkfl_nqf(temp_ratings)

    return ans

def wkfl_znv(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3185:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3186), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3185)))

    return ans

def wkfl_dhr(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1967:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1966)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1967), part_ratings.m.r))
    
    ans += part_ratings.total

    return ans

def wkfl_bz(part_ratings: PartRatings) -> int:
    ans = 0

    # m<635:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 634)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 635), part_ratings.m.r))
    
    ans += part_ratings.total

    return ans

def wkfl_nv(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2204:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2203)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2204), part_ratings.s.r))
    
    ans += wkfl_jd(part_ratings)

    return ans

def wkfl_flh(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2334:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2333)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2334), part_ratings.x.r))
    
    # x<2934:vqg
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2933)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2934), part_ratings.x.r))
    ans += wkfl_vqg(temp_ratings)

    return ans

def wkfl_stj(part_ratings: PartRatings) -> int:
    ans = 0

    # x>736:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 737), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 736)))

    return ans

def wkfl_gd(part_ratings: PartRatings) -> int:
    ans = 0

    # a<459:fn
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 458)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 459), part_ratings.a.r))
    ans += wkfl_fn(temp_ratings)
    
    # m<1741:rb
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1740)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1741), part_ratings.m.r))
    ans += wkfl_rb(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_ngt(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2607:hjl
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2606)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2607), part_ratings.x.r))
    ans += wkfl_hjl(temp_ratings)
    
    # s>1104:zmr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1105), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1104)))
    ans += wkfl_zmr(temp_ratings)
    
    ans += wkfl_xrx(part_ratings)

    return ans

def wkfl_vf(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1654:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1655), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1654)))
    ans += temp_ratings.total
    
    # s<1631:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1630)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1631), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_bv(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2721:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2720)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2721), part_ratings.a.r))
    ans += temp_ratings.total
    
    # a>2828:mmh
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2829), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2828)))
    ans += wkfl_mmh(temp_ratings)
    
    ans += wkfl_gb(part_ratings)

    return ans

def wkfl_sff(part_ratings: PartRatings) -> int:
    ans = 0

    # m>680:jv
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 681), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 680)))
    ans += wkfl_jv(temp_ratings)
    
    # a<2906:tc
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2905)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2906), part_ratings.a.r))
    ans += wkfl_tc(temp_ratings)
    
    # s<325:lrf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 324)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 325), part_ratings.s.r))
    ans += wkfl_lrf(temp_ratings)
    
    ans += wkfl_qlp(part_ratings)

    return ans

def wkfl_zct(part_ratings: PartRatings) -> int:
    ans = 0

    # a<456:hkq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 455)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 456), part_ratings.a.r))
    ans += wkfl_hkq(temp_ratings)
    
    # a<500:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 499)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 500), part_ratings.a.r))
    
    # x<2109:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2108)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2109), part_ratings.x.r))
    
    ans += wkfl_lbl(part_ratings)

    return ans

def wkfl_tjz(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2497:zb
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2496)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2497), part_ratings.m.r))
    ans += wkfl_zb(temp_ratings)
    
    ans += wkfl_hx(part_ratings)

    return ans

def wkfl_dgf(part_ratings: PartRatings) -> int:
    ans = 0

    # a>187:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 188), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 187)))
    
    # s<1048:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1047)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1048), part_ratings.s.r))

    return ans

def wkfl_jg(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2301:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2302), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2301)))
    ans += temp_ratings.total
    
    # s>3370:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3371), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3370)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_zj(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1836:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1837), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1836)))

    return ans

def wkfl_tnt(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2872:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2873), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2872)))
    ans += temp_ratings.total
    
    # a>3297:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3298), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3297)))
    ans += temp_ratings.total
    
    # x<2235:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2234)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2235), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_qvc(part_ratings: PartRatings) -> int:
    ans = 0

    # m<67:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 66)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 67), part_ratings.m.r))
    
    ans += part_ratings.total

    return ans

def wkfl_xnb(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1928:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1929), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1928)))
    
    # s>2287:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2288), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2287)))
    ans += temp_ratings.total
    
    # x<739:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 738)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 739), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_ntr(part_ratings: PartRatings) -> int:
    ans = 0

    # m>181:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 182), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 181)))
    ans += temp_ratings.total
    
    # a<2441:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2440)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2441), part_ratings.a.r))
    
    ans += part_ratings.total

    return ans

def wkfl_blt(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1980:vk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1979)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1980), part_ratings.x.r))
    ans += wkfl_vk(temp_ratings)
    
    # m<2092:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2091)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2092), part_ratings.m.r))
    
    ans += wkfl_vrb(part_ratings)

    return ans

def wkfl_tbx(part_ratings: PartRatings) -> int:
    ans = 0

    # a>423:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 424), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 423)))
    
    # s<3681:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3680)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3681), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_rj(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1380:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1381), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1380)))
    ans += temp_ratings.total
    
    # s>2867:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2868), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2867)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_rk(part_ratings: PartRatings) -> int:
    ans = 0

    # m>133:gvd
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 134), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 133)))
    ans += wkfl_gvd(temp_ratings)
    
    ans += wkfl_mgk(part_ratings)

    return ans

def wkfl_rf(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1036:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1037), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1036)))

    return ans

def wkfl_ztt(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1176:jn
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1175)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1176), part_ratings.a.r))
    ans += wkfl_jn(temp_ratings)
    
    ans += wkfl_pd(part_ratings)

    return ans

def wkfl_xzp(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1694:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1695), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1694)))
    
    # a>2561:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2562), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2561)))

    return ans

def wkfl_hpf(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1058:qlg
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1057)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1058), part_ratings.s.r))
    ans += wkfl_qlg(temp_ratings)
    
    # m>2212:zcq
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2213), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2212)))
    ans += wkfl_zcq(temp_ratings)
    
    ans += wkfl_blt(part_ratings)

    return ans

def wkfl_nz(part_ratings: PartRatings) -> int:
    ans = 0

    # s<915:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 914)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 915), part_ratings.s.r))
    
    # x>3243:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3244), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3243)))
    
    ans += part_ratings.total

    return ans

def wkfl_ptx(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1510:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1511), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1510)))
    ans += temp_ratings.total
    
    # x<1938:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1937)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1938), part_ratings.x.r))
    
    # s<1664:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1663)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1664), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_dd(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1074:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1073)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1074), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_nms(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1665:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1664)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1665), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s<1707:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1706)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1707), part_ratings.s.r))
    
    # x<2042:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2041)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2042), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_tnf(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3502:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3501)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3502), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_gsr(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1002:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1001)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1002), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s>1019:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1020), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1019)))
    
    # a<1034:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1033)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1034), part_ratings.a.r))
    
    ans += part_ratings.total

    return ans

def wkfl_dl(part_ratings: PartRatings) -> int:
    ans = 0

    # s>3490:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3491), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3490)))
    ans += temp_ratings.total
    
    ans += wkfl_hgb(part_ratings)

    return ans

def wkfl_ccx(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2085:hjv
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2086), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2085)))
    ans += wkfl_hjv(temp_ratings)
    
    # x>2074:sj
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2075), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2074)))
    ans += wkfl_sj(temp_ratings)
    
    ans += wkfl_ft(part_ratings)

    return ans

def wkfl_bsz(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1011:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1010)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1011), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_krq(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1856:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1857), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1856)))
    ans += temp_ratings.total

    return ans

def wkfl_fpm(part_ratings: PartRatings) -> int:
    ans = 0

    # x>911:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 912), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 911)))
    
    # s>2561:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2562), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2561)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_tks(part_ratings: PartRatings) -> int:
    ans = 0

    # a<68:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 67)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 68), part_ratings.a.r))
    
    # x<3159:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3158)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3159), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_mb(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2309:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2310), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2309)))
    
    # a>794:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 795), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 794)))
    ans += temp_ratings.total
    
    # m>422:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 423), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 422)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_tm(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3640:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3639)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3640), part_ratings.m.r))
    ans += temp_ratings.total
    
    # a>38:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 39), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 38)))
    ans += temp_ratings.total
    
    # a>24:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 25), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 24)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_jd(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2635:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2634)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2635), part_ratings.s.r))
    
    # s>2861:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2862), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2861)))
    ans += temp_ratings.total
    
    # x<2444:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2443)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2444), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_cl(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1487:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1486)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1487), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_ks(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3873:hvl
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3874), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3873)))
    ans += wkfl_hvl(temp_ratings)
    
    # s>2520:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2521), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2520)))
    ans += temp_ratings.total
    
    ans += wkfl_xp(part_ratings)

    return ans

def wkfl_pl(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1634:qb
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1635), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1634)))
    ans += wkfl_qb(temp_ratings)
    
    # a>1976:rgn
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1977), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1976)))
    ans += wkfl_rgn(temp_ratings)
    
    ans += wkfl_kx(part_ratings)

    return ans

def wkfl_sq(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1062:kd
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1063), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1062)))
    ans += wkfl_kd(temp_ratings)
    
    # m>933:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 934), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 933)))
    ans += temp_ratings.total
    
    ans += wkfl_fl(part_ratings)

    return ans

def wkfl_bf(part_ratings: PartRatings) -> int:
    ans = 0

    # m<295:qlq
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 294)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 295), part_ratings.m.r))
    ans += wkfl_qlq(temp_ratings)
    
    ans += wkfl_gxr(part_ratings)

    return ans

def wkfl_qb(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2051:nsh
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2052), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2051)))
    ans += wkfl_nsh(temp_ratings)
    
    # m>2598:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2599), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2598)))
    ans += temp_ratings.total
    
    # s<3081:ts
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3080)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3081), part_ratings.s.r))
    ans += wkfl_ts(temp_ratings)
    
    ans += wkfl_hmj(part_ratings)

    return ans

def wkfl_pz(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1077:rtf
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1076)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1077), part_ratings.x.r))
    ans += wkfl_rtf(temp_ratings)
    
    ans += wkfl_xg(part_ratings)

    return ans

def wkfl_dqp(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1009:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1010), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1009)))
    
    # s<1679:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1678)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1679), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_hcs(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2525:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2524)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2525), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s>3056:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3057), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3056)))
    
    # a<2896:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2895)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2896), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_vzt(part_ratings: PartRatings) -> int:
    ans = 0

    # m>486:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 487), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 486)))
    
    # m>406:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 407), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 406)))
    ans += temp_ratings.total

    return ans

def wkfl_cpt(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1917:rpf
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1918), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1917)))
    ans += wkfl_rpf(temp_ratings)
    
    ans += wkfl_pt(part_ratings)

    return ans

def wkfl_kqc(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1059:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1060), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1059)))
    
    # s<2314:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2313)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2314), part_ratings.s.r))
    ans += temp_ratings.total
    
    # m<856:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 855)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 856), part_ratings.m.r))

    return ans

def wkfl_qlp(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2076:xl
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2075)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2076), part_ratings.x.r))
    ans += wkfl_xl(temp_ratings)
    
    # s>456:bf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 457), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 456)))
    ans += wkfl_bf(temp_ratings)
    
    ans += wkfl_smp(part_ratings)

    return ans

def wkfl_smp(part_ratings: PartRatings) -> int:
    ans = 0

    # m>381:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 382), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 381)))
    
    # a>3571:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3572), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3571)))
    ans += temp_ratings.total

    return ans

def wkfl_kf(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3449:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3448)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3449), part_ratings.a.r))
    
    # x>2649:fj
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2650), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2649)))
    ans += wkfl_fj(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_zmb(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3595:fd
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3594)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3595), part_ratings.s.r))
    ans += wkfl_fd(temp_ratings)
    
    # m>373:xtk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 374), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 373)))
    ans += wkfl_xtk(temp_ratings)
    
    ans += wkfl_sdj(part_ratings)

    return ans

def wkfl_lb(part_ratings: PartRatings) -> int:
    ans = 0

    # a>760:bpj
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 761), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 760)))
    ans += wkfl_bpj(temp_ratings)
    
    # s>1094:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1095), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1094)))
    ans += temp_ratings.total
    
    ans += wkfl_cqh(part_ratings)

    return ans

def wkfl_zmt(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2607:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2606)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2607), part_ratings.a.r))
    
    # x<2494:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2493)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2494), part_ratings.x.r))
    
    # x<2625:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2624)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2625), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_hrs(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3442:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3441)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3442), part_ratings.s.r))
    ans += temp_ratings.total
    
    # m<2938:rx
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2937)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2938), part_ratings.m.r))
    ans += wkfl_rx(temp_ratings)

    return ans

def wkfl_vs(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1022:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1023), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1022)))
    ans += temp_ratings.total
    
    # m<1556:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1555)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1556), part_ratings.m.r))

    return ans

def wkfl_tj(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2713:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2714), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2713)))
    
    # a>2515:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2516), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2515)))
    ans += temp_ratings.total
    
    # s<1508:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1507)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1508), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_vg(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1861:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1862), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1861)))
    ans += temp_ratings.total

    return ans

def wkfl_hsz(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2662:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2663), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2662)))
    
    # x<2851:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2850)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2851), part_ratings.x.r))
    ans += temp_ratings.total
    
    # x<3435:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3434)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3435), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_fj(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1691:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1690)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1691), part_ratings.m.r))

    return ans

def wkfl_sbl(part_ratings: PartRatings) -> int:
    ans = 0

    # s<559:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 558)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 559), part_ratings.s.r))
    
    # s>786:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 787), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 786)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_pbt(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2656:kkl
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2657), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2656)))
    ans += wkfl_kkl(temp_ratings)
    
    # a>1768:qhv
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1769), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1768)))
    ans += wkfl_qhv(temp_ratings)
    
    ans += wkfl_xt(part_ratings)

    return ans

def wkfl_lhl(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1684:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1685), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1684)))

    return ans

def wkfl_clg(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1239:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1240), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1239)))
    ans += temp_ratings.total
    
    # s<1688:jdk
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1687)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1688), part_ratings.s.r))
    ans += wkfl_jdk(temp_ratings)
    
    # a<489:xr
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 488)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 489), part_ratings.a.r))
    ans += wkfl_xr(temp_ratings)

    return ans

def wkfl_hxc(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2077:jp
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2078), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2077)))
    ans += wkfl_jp(temp_ratings)
    
    # s<1527:zjg
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1526)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1527), part_ratings.s.r))
    ans += wkfl_zjg(temp_ratings)
    
    ans += wkfl_lxm(part_ratings)

    return ans

def wkfl_zl(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2468:rmq
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2469), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2468)))
    ans += wkfl_rmq(temp_ratings)
    
    # x<1255:pr
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1254)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1255), part_ratings.x.r))
    ans += wkfl_pr(temp_ratings)
    
    # s<399:cdh
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 398)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 399), part_ratings.s.r))
    ans += wkfl_cdh(temp_ratings)
    
    ans += wkfl_gz(part_ratings)

    return ans

def wkfl_vmk(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2804:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2805), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2804)))
    
    # a<798:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 797)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 798), part_ratings.a.r))
    
    # a>1792:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1793), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1792)))
    
    ans += part_ratings.total

    return ans

def wkfl_xjb(part_ratings: PartRatings) -> int:
    ans = 0

    # m<580:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 579)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 580), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_dfq(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2644:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2643)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2644), part_ratings.s.r))
    ans += temp_ratings.total
    
    # a<1846:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1845)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1846), part_ratings.a.r))
    ans += temp_ratings.total
    
    # s<3186:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3185)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3186), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_jdk(part_ratings: PartRatings) -> int:
    ans = 0

    # a>538:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 539), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 538)))
    ans += temp_ratings.total
    
    # s>1662:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1663), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1662)))
    
    ans += part_ratings.total

    return ans

def wkfl_cbr(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2499:rqp
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2498)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2499), part_ratings.m.r))
    ans += wkfl_rqp(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_fzt(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2823:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2822)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2823), part_ratings.m.r))
    
    # s<2719:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2718)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2719), part_ratings.s.r))
    
    # s<2989:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2988)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2989), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_kx(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1487:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1486)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1487), part_ratings.x.r))
    ans += temp_ratings.total
    
    # x>1580:hrd
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1581), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1580)))
    ans += wkfl_hrd(temp_ratings)
    
    # s>3205:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3206), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3205)))
    
    ans += wkfl_hr(part_ratings)

    return ans

def wkfl_mdc(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2678:vb
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2679), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2678)))
    ans += wkfl_vb(temp_ratings)
    
    # x<479:bqt
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 478)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 479), part_ratings.x.r))
    ans += wkfl_bqt(temp_ratings)
    
    # x<661:xd
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 660)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 661), part_ratings.x.r))
    ans += wkfl_xd(temp_ratings)
    
    ans += wkfl_jkv(part_ratings)

    return ans

def wkfl_db(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3443:jbt
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3444), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3443)))
    ans += wkfl_jbt(temp_ratings)
    
    # x<2147:dr
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2146)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2147), part_ratings.x.r))
    ans += wkfl_dr(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_ptz(part_ratings: PartRatings) -> int:
    ans = 0

    # m>292:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 293), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 292)))
    ans += temp_ratings.total
    
    # x<2852:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2851)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2852), part_ratings.x.r))
    ans += temp_ratings.total
    
    # m>275:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 276), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 275)))
    ans += temp_ratings.total

    return ans

def wkfl_pk(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2230:rd
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2231), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2230)))
    ans += wkfl_rd(temp_ratings)
    
    # s>1596:gfx
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1597), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1596)))
    ans += wkfl_gfx(temp_ratings)
    
    # x>881:nbz
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 882), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 881)))
    ans += wkfl_nbz(temp_ratings)
    
    ans += wkfl_khh(part_ratings)

    return ans

def wkfl_ggg(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1517:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1518), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1517)))
    
    # x<158:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 157)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 158), part_ratings.x.r))
    
    # s<1333:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1332)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1333), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_lx(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2306:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2307), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2306)))
    ans += temp_ratings.total
    
    # s<930:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 929)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 930), part_ratings.s.r))
    
    # s<1289:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1288)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1289), part_ratings.s.r))

    return ans

def wkfl_pf(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2169:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2170), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2169)))
    ans += temp_ratings.total

    return ans

def wkfl_bl(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1235:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1234)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1235), part_ratings.m.r))
    ans += temp_ratings.total
    
    # x<618:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 617)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 618), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_kgp(part_ratings: PartRatings) -> int:
    ans = 0

    # x>3660:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3661), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3660)))
    ans += temp_ratings.total
    
    # m<2117:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2116)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2117), part_ratings.m.r))
    
    # a>787:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 788), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 787)))

    return ans

def wkfl_gtt(part_ratings: PartRatings) -> int:
    ans = 0

    # a<821:jsm
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 820)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 821), part_ratings.a.r))
    ans += wkfl_jsm(temp_ratings)
    
    # m<1415:lm
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1414)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1415), part_ratings.m.r))
    ans += wkfl_lm(temp_ratings)
    
    ans += wkfl_hrj(part_ratings)

    return ans

def wkfl_np(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1026:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1027), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1026)))
    ans += temp_ratings.total
    
    # a<537:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 536)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 537), part_ratings.a.r))
    ans += temp_ratings.total
    
    # s>3199:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3200), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3199)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_qs(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2059:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2060), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2059)))
    ans += temp_ratings.total
    
    # a>3426:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3427), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3426)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_vk(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1173:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1172)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1173), part_ratings.x.r))
    
    # s<1371:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1370)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1371), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_dtm(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3399:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3400), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3399)))
    ans += temp_ratings.total
    
    # x>1063:fzt
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1064), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1063)))
    ans += wkfl_fzt(temp_ratings)

    return ans

def wkfl_bph(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1636:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1635)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1636), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_hn(part_ratings: PartRatings) -> int:
    ans = 0

    # s>755:gh
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 756), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 755)))
    ans += wkfl_gh(temp_ratings)
    
    ans += wkfl_lth(part_ratings)

    return ans

def wkfl_gn(part_ratings: PartRatings) -> int:
    ans = 0

    # x<240:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 239)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 240), part_ratings.x.r))
    ans += temp_ratings.total
    
    # s<313:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 312)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 313), part_ratings.s.r))

    return ans

def wkfl_hng(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1990:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1991), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1990)))
    ans += temp_ratings.total
    
    # a>1724:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1725), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1724)))
    
    # s>1865:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1866), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1865)))
    ans += temp_ratings.total

    return ans

def wkfl_vxl(part_ratings: PartRatings) -> int:
    ans = 0

    # a>475:xn
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 476), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 475)))
    ans += wkfl_xn(temp_ratings)
    
    # a<174:mrh
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 173)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 174), part_ratings.a.r))
    ans += wkfl_mrh(temp_ratings)
    
    ans += wkfl_sn(part_ratings)

    return ans

def wkfl_mg(part_ratings: PartRatings) -> int:
    ans = 0

    # a>55:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 56), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 55)))
    
    # x>1083:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1084), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1083)))
    
    ans += part_ratings.total

    return ans

def wkfl_dqn(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1522:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1521)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1522), part_ratings.s.r))
    
    # a<707:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 706)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 707), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_xmz(part_ratings: PartRatings) -> int:
    ans = 0

    # x>885:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 886), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 885)))
    
    # a>3671:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3672), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3671)))
    
    ans += part_ratings.total

    return ans

def wkfl_dnn(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2403:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2404), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2403)))
    
    # m>381:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 382), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 381)))
    ans += temp_ratings.total
    
    # s<317:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 316)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 317), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_knx(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2648:jvp
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2649), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2648)))
    ans += wkfl_jvp(temp_ratings)
    
    # s>1655:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1656), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1655)))
    
    ans += part_ratings.total

    return ans

def wkfl_mr(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1887:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1888), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1887)))
    ans += temp_ratings.total
    
    # s>1800:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1801), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1800)))
    
    # x>1621:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1622), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1621)))

    return ans

def wkfl_cgz(part_ratings: PartRatings) -> int:
    ans = 0

    # a<334:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 333)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 334), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_tn(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1209:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1210), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1209)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_rx(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2648:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2647)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2648), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s<3802:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3801)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3802), part_ratings.s.r))

    return ans

def wkfl_ljj(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2311:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2312), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2311)))
    
    # a>1322:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1323), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1322)))

    return ans

def wkfl_ccj(part_ratings: PartRatings) -> int:
    ans = 0

    # a<897:gtt
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 896)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 897), part_ratings.a.r))
    ans += wkfl_gtt(temp_ratings)
    
    ans += wkfl_pgs(part_ratings)

    return ans

def wkfl_sf(part_ratings: PartRatings) -> int:
    ans = 0

    # x<828:ffd
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 827)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 828), part_ratings.x.r))
    ans += wkfl_ffd(temp_ratings)

    return ans

def wkfl_kk(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2309:ld
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2308)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2309), part_ratings.a.r))
    ans += wkfl_ld(temp_ratings)
    
    # x<650:hc
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 649)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 650), part_ratings.x.r))
    ans += wkfl_hc(temp_ratings)
    
    ans += wkfl_gm(part_ratings)

    return ans

def wkfl_sd(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3490:gdc
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3489)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3490), part_ratings.s.r))
    ans += wkfl_gdc(temp_ratings)
    
    # m>86:xc
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 87), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 86)))
    ans += wkfl_xc(temp_ratings)
    
    # s>3727:ztt
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3728), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3727)))
    ans += wkfl_ztt(temp_ratings)
    
    ans += wkfl_ldb(part_ratings)

    return ans

def wkfl_frt(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1622:zlj
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1623), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1622)))
    ans += wkfl_zlj(temp_ratings)
    
    # s<1199:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1198)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1199), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_hkq(part_ratings: PartRatings) -> int:
    ans = 0

    # a<422:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 421)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 422), part_ratings.a.r))
    
    # m<1595:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1594)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1595), part_ratings.m.r))

    return ans

def wkfl_ffd(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1595:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1594)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1595), part_ratings.a.r))
    
    ans += part_ratings.total

    return ans

def wkfl_jt(part_ratings: PartRatings) -> int:
    ans = 0

    # a>779:cm
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 780), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 779)))
    ans += wkfl_cm(temp_ratings)
    
    ans += wkfl_sbh(part_ratings)

    return ans

def wkfl_bfh(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1742:grb
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1741)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1742), part_ratings.m.r))
    ans += wkfl_grb(temp_ratings)
    
    # x>3013:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3014), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3013)))

    return ans

def wkfl_lk(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1946:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1947), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1946)))
    ans += temp_ratings.total
    
    # m>147:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 148), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 147)))
    ans += temp_ratings.total

    return ans

def wkfl_gtd(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2429:dq
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2430), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2429)))
    ans += wkfl_dq(temp_ratings)
    
    # s>2097:xz
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2098), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2097)))
    ans += wkfl_xz(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_zk(part_ratings: PartRatings) -> int:
    ans = 0

    # m>221:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 222), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 221)))
    
    # m<123:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 122)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 123), part_ratings.m.r))
    
    # x<3107:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3106)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3107), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_mk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3811:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3810)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3811), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_rbk(part_ratings: PartRatings) -> int:
    ans = 0

    # x>3208:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3209), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3208)))
    ans += temp_ratings.total

    return ans

def wkfl_bst(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2634:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2635), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2634)))
    
    # x<965:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 964)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 965), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_br(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3155:ghz
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3156), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3155)))
    ans += wkfl_ghz(temp_ratings)
    
    ans += wkfl_ngt(part_ratings)

    return ans

def wkfl_krj(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2941:dk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2940)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2941), part_ratings.m.r))
    ans += wkfl_dk(temp_ratings)
    
    ans += wkfl_ppr(part_ratings)

    return ans

def wkfl_jzf(part_ratings: PartRatings) -> int:
    ans = 0

    # s<286:plr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 285)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 286), part_ratings.s.r))
    ans += wkfl_plr(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_hdl(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1800:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1801), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1800)))
    
    # x<531:fsf
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 530)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 531), part_ratings.x.r))
    ans += wkfl_fsf(temp_ratings)
    
    ans += wkfl_mx(part_ratings)

    return ans

def wkfl_vlt(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1646:sr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1647), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1646)))
    ans += wkfl_sr(temp_ratings)
    
    # a<808:dqn
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 807)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 808), part_ratings.a.r))
    ans += wkfl_dqn(temp_ratings)

    return ans

def wkfl_pgc(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3070:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3071), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3070)))
    ans += temp_ratings.total

    return ans

def wkfl_zbh(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1505:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1506), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1505)))
    
    ans += part_ratings.total

    return ans

def wkfl_szx(part_ratings: PartRatings) -> int:
    ans = 0

    # s<371:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 370)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 371), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_xpf(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2983:gt
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2982)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2983), part_ratings.x.r))
    ans += wkfl_gt(temp_ratings)
    
    # x<3494:lrv
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3493)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3494), part_ratings.x.r))
    ans += wkfl_lrv(temp_ratings)
    
    ans += wkfl_jr(part_ratings)

    return ans

def wkfl_cd(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3395:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3396), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3395)))

    return ans

def wkfl_in(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1748:vh
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1749), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1748)))
    ans += wkfl_vh(temp_ratings)
    
    ans += wkfl_th(part_ratings)

    return ans

def wkfl_gb(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2761:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2762), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2761)))
    ans += temp_ratings.total
    
    # x<1367:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1366)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1367), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_sxn(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1528:tq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1529), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1528)))
    ans += wkfl_tq(temp_ratings)
    
    ans += wkfl_bdm(part_ratings)

    return ans

def wkfl_ft(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2464:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2463)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2464), part_ratings.m.r))
    
    # s<669:cr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 668)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 669), part_ratings.s.r))
    ans += wkfl_cr(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_njp(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2512:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2513), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2512)))
    ans += temp_ratings.total
    
    # m>3390:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3391), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3390)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_vj(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2188:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2187)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2188), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_gv(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1415:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1414)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1415), part_ratings.x.r))
    
    # s>3684:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3685), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3684)))
    ans += temp_ratings.total
    
    # a>73:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 74), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 73)))

    return ans

def wkfl_bjb(part_ratings: PartRatings) -> int:
    ans = 0

    # m<782:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 781)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 782), part_ratings.m.r))
    ans += temp_ratings.total

    return ans

def wkfl_jzq(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1538:sbz
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1539), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1538)))
    ans += wkfl_sbz(temp_ratings)
    
    ans += wkfl_jt(part_ratings)

    return ans

def wkfl_qnt(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1849:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1850), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1849)))
    ans += temp_ratings.total
    
    # s>3148:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3149), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3148)))
    
    ans += part_ratings.total

    return ans

def wkfl_rb(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1030:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1029)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1030), part_ratings.m.r))
    ans += temp_ratings.total
    
    # a>515:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 516), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 515)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_hqb(part_ratings: PartRatings) -> int:
    ans = 0

    # a>180:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 181), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 180)))
    ans += temp_ratings.total
    
    # x<2462:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2461)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2462), part_ratings.x.r))
    ans += temp_ratings.total
    
    # s<776:ggm
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 775)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 776), part_ratings.s.r))
    ans += wkfl_ggm(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_qsp(part_ratings: PartRatings) -> int:
    ans = 0

    # a>517:ljt
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 518), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 517)))
    ans += wkfl_ljt(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_dj(part_ratings: PartRatings) -> int:
    ans = 0

    # a<479:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 478)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 479), part_ratings.a.r))

    return ans

def wkfl_ms(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1531:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1530)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1531), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_fx(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1676:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1677), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1676)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_xh(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1028:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1027)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1028), part_ratings.a.r))
    
    # s<1208:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1207)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1208), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_td(part_ratings: PartRatings) -> int:
    ans = 0

    # s<279:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 278)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 279), part_ratings.s.r))
    
    # s>309:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 310), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 309)))
    
    # m<559:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 558)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 559), part_ratings.m.r))
    
    ans += part_ratings.total

    return ans

def wkfl_jxs(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1040:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1041), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1040)))
    
    # x<1013:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1012)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1013), part_ratings.x.r))
    ans += temp_ratings.total
    
    # x>1442:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1443), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1442)))

    return ans

def wkfl_zbx(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1180:jkd
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1181), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1180)))
    ans += wkfl_jkd(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_bfz(part_ratings: PartRatings) -> int:
    ans = 0

    # s<963:vjx
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 962)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 963), part_ratings.s.r))
    ans += wkfl_vjx(temp_ratings)
    
    # s<1451:kmf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1450)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1451), part_ratings.s.r))
    ans += wkfl_kmf(temp_ratings)
    
    # a<644:jcq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 643)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 644), part_ratings.a.r))
    ans += wkfl_jcq(temp_ratings)
    
    ans += wkfl_ppv(part_ratings)

    return ans

def wkfl_tx(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2961:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2962), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2961)))
    ans += temp_ratings.total
    
    # x>2724:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2725), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2724)))
    
    # s>1722:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1723), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1722)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_th(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2282:vlx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2283), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2282)))
    ans += wkfl_vlx(temp_ratings)
    
    # a>1079:pbt
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1080), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1079)))
    ans += wkfl_pbt(temp_ratings)
    
    # a>361:bfz
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 362), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 361)))
    ans += wkfl_bfz(temp_ratings)
    
    ans += wkfl_fhl(part_ratings)

    return ans

def wkfl_nh(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1964:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1963)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1964), part_ratings.x.r))
    
    # m>1122:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1123), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1122)))

    return ans

def wkfl_mcs(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2425:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2424)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2425), part_ratings.a.r))
    
    # a>2964:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2965), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2964)))
    
    # m>3001:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3002), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3001)))
    
    ans += wkfl_zmt(part_ratings)

    return ans

def wkfl_pj(part_ratings: PartRatings) -> int:
    ans = 0

    # m>623:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 624), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 623)))
    ans += temp_ratings.total
    
    # a>3740:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3741), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3740)))
    
    ans += part_ratings.total

    return ans

def wkfl_czz(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1674:px
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1675), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1674)))
    ans += wkfl_px(temp_ratings)
    
    ans += wkfl_kb(part_ratings)

    return ans

def wkfl_ktp(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3783:grj
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3782)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3783), part_ratings.m.r))
    ans += wkfl_grj(temp_ratings)
    
    # m>3903:vlq
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3904), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3903)))
    ans += wkfl_vlq(temp_ratings)
    
    # m>3825:ks
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3826), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3825)))
    ans += wkfl_ks(temp_ratings)
    
    ans += wkfl_jb(part_ratings)

    return ans

def wkfl_shf(part_ratings: PartRatings) -> int:
    ans = 0

    # s<649:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 648)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 649), part_ratings.s.r))
    
    # m<1371:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1370)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1371), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s<894:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 893)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 894), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_xg(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1515:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1516), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1515)))
    
    # x<1605:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1604)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1605), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_bb(part_ratings: PartRatings) -> int:
    ans = 0

    # m>400:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 401), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 400)))
    
    # a>117:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 118), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 117)))
    
    # a<43:xsk
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 42)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 43), part_ratings.a.r))
    ans += wkfl_xsk(temp_ratings)
    
    ans += wkfl_gv(part_ratings)

    return ans

def wkfl_vt(part_ratings: PartRatings) -> int:
    ans = 0

    # x>3630:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3631), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3630)))
    
    # x<3347:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3346)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3347), part_ratings.x.r))
    
    # a<2164:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2163)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2164), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_jv(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1524:sq
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1525), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1524)))
    ans += wkfl_sq(temp_ratings)
    
    # x<632:bp
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 631)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 632), part_ratings.x.r))
    ans += wkfl_bp(temp_ratings)
    
    # a>3325:zbx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3326), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3325)))
    ans += wkfl_zbx(temp_ratings)
    
    ans += wkfl_jzf(part_ratings)

    return ans

def wkfl_trk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3156:nxr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3155)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3156), part_ratings.s.r))
    ans += wkfl_nxr(temp_ratings)
    
    # m>186:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 187), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 186)))
    
    ans += wkfl_rz(part_ratings)

    return ans

def wkfl_jkv(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2135:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2136), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2135)))
    
    # x<847:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 846)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 847), part_ratings.x.r))
    ans += temp_ratings.total
    
    # m<907:bjb
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 906)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 907), part_ratings.m.r))
    ans += wkfl_bjb(temp_ratings)
    
    ans += wkfl_hng(part_ratings)

    return ans

def wkfl_fs(part_ratings: PartRatings) -> int:
    ans = 0

    # s>731:mg
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 732), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 731)))
    ans += wkfl_mg(temp_ratings)
    
    # a>75:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 76), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 75)))
    
    # s>329:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 330), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 329)))
    ans += temp_ratings.total
    
    ans += wkfl_tm(part_ratings)

    return ans

def wkfl_sfh(part_ratings: PartRatings) -> int:
    ans = 0

    # s<738:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 737)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 738), part_ratings.s.r))
    
    # m>2004:bvg
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2005), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2004)))
    ans += wkfl_bvg(temp_ratings)
    
    # s<824:jx
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 823)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 824), part_ratings.s.r))
    ans += wkfl_jx(temp_ratings)

    return ans

def wkfl_khh(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1520:ndz
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1519)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1520), part_ratings.s.r))
    ans += wkfl_ndz(temp_ratings)
    
    # s>1564:xk
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1565), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1564)))
    ans += wkfl_xk(temp_ratings)
    
    # a>825:hqs
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 826), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 825)))
    ans += wkfl_hqs(temp_ratings)
    
    ans += wkfl_snc(part_ratings)

    return ans

def wkfl_vmt(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1060:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1061), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1060)))
    ans += temp_ratings.total

    return ans

def wkfl_xtn(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2734:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2735), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2734)))
    ans += temp_ratings.total
    
    # a<2487:xcd
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2486)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2487), part_ratings.a.r))
    ans += wkfl_xcd(temp_ratings)
    
    # s<942:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 941)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 942), part_ratings.s.r))
    
    ans += wkfl_jsk(part_ratings)

    return ans

def wkfl_pv(part_ratings: PartRatings) -> int:
    ans = 0

    # m<225:sxh
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 224)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 225), part_ratings.m.r))
    ans += wkfl_sxh(temp_ratings)
    
    # s<3025:vxl
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3024)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3025), part_ratings.s.r))
    ans += wkfl_vxl(temp_ratings)
    
    # a<625:mn
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 624)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 625), part_ratings.a.r))
    ans += wkfl_mn(temp_ratings)
    
    ans += wkfl_zmb(part_ratings)

    return ans

def wkfl_mbh(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2984:pnp
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2985), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2984)))
    ans += wkfl_pnp(temp_ratings)
    
    # m<2727:cbr
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2726)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2727), part_ratings.m.r))
    ans += wkfl_cbr(temp_ratings)
    
    # a>2966:zc
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2967), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2966)))
    ans += wkfl_zc(temp_ratings)
    
    ans += wkfl_kq(part_ratings)

    return ans

def wkfl_tz(part_ratings: PartRatings) -> int:
    ans = 0

    # x>736:lxc
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 737), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 736)))
    ans += wkfl_lxc(temp_ratings)

    return ans

def wkfl_ns(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2974:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2975), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2974)))
    
    # a>1996:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1997), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1996)))
    ans += temp_ratings.total

    return ans

def wkfl_zs(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2274:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2273)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2274), part_ratings.s.r))
    
    # m<2653:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2652)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2653), part_ratings.m.r))
    
    # m>2890:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2891), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2890)))
    ans += temp_ratings.total

    return ans

def wkfl_hjv(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1376:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1375)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1376), part_ratings.m.r))
    
    # m<2830:snd
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2829)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2830), part_ratings.m.r))
    ans += wkfl_snd(temp_ratings)
    
    # x<2077:vj
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2076)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2077), part_ratings.x.r))
    ans += wkfl_vj(temp_ratings)

    return ans

def wkfl_vh(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2348:fcr
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2349), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2348)))
    ans += wkfl_fcr(temp_ratings)
    
    # m>1339:dp
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1340), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1339)))
    ans += wkfl_dp(temp_ratings)
    
    ans += wkfl_rrl(part_ratings)

    return ans

def wkfl_fhl(part_ratings: PartRatings) -> int:
    ans = 0

    # a>214:hn
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 215), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 214)))
    ans += wkfl_hn(temp_ratings)
    
    # m<1951:hs
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1950)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1951), part_ratings.m.r))
    ans += wkfl_hs(temp_ratings)
    
    ans += wkfl_br(part_ratings)

    return ans

def wkfl_vrj(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1124:sf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1123)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1124), part_ratings.s.r))
    ans += wkfl_sf(temp_ratings)
    
    # x<615:gtk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 614)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 615), part_ratings.x.r))
    ans += wkfl_gtk(temp_ratings)
    
    ans += wkfl_krq(part_ratings)

    return ans

def wkfl_lh(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1638:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1639), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1638)))
    
    # a<732:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 731)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 732), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_xtk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3861:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3860)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3861), part_ratings.s.r))
    ans += temp_ratings.total
    
    # x>1489:lkb
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1490), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1489)))
    ans += wkfl_lkb(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_zq(part_ratings: PartRatings) -> int:
    ans = 0

    # a>832:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 833), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 832)))
    
    # m>69:qhk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 70), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 69)))
    ans += wkfl_qhk(temp_ratings)
    
    ans += wkfl_rrc(part_ratings)

    return ans

def wkfl_lm(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1458:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1459), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1458)))
    ans += temp_ratings.total
    
    # x>685:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 686), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 685)))
    ans += temp_ratings.total
    
    # s>1314:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1315), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1314)))

    return ans

def wkfl_czd(part_ratings: PartRatings) -> int:
    ans = 0

    # s<489:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 488)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 489), part_ratings.s.r))
    ans += temp_ratings.total
    
    # x>2594:zv
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2595), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2594)))
    ans += wkfl_zv(temp_ratings)
    
    ans += wkfl_vhb(part_ratings)

    return ans

def wkfl_gfx(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1694:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1695), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1694)))
    ans += temp_ratings.total
    
    # a>839:bph
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 840), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 839)))
    ans += wkfl_bph(temp_ratings)
    
    # x<1229:lh
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1228)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1229), part_ratings.x.r))
    ans += wkfl_lh(temp_ratings)
    
    ans += wkfl_vsz(part_ratings)

    return ans

def wkfl_ngr(part_ratings: PartRatings) -> int:
    ans = 0

    # x>3139:vf
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3140), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3139)))
    ans += wkfl_vf(temp_ratings)

    return ans

def wkfl_sr(part_ratings: PartRatings) -> int:
    ans = 0

    # a<801:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 800)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 801), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_vlq(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1769:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1770), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1769)))
    ans += temp_ratings.total
    
    # a<621:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 620)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 621), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += wkfl_rf(part_ratings)

    return ans

def wkfl_xpd(part_ratings: PartRatings) -> int:
    ans = 0

    # x>3380:znv
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3381), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3380)))
    ans += wkfl_znv(temp_ratings)
    
    ans += wkfl_ct(part_ratings)

    return ans

def wkfl_vjx(part_ratings: PartRatings) -> int:
    ans = 0

    # a<669:gmx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 668)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 669), part_ratings.a.r))
    ans += wkfl_gmx(temp_ratings)
    
    ans += wkfl_zl(part_ratings)

    return ans

def wkfl_gmx(part_ratings: PartRatings) -> int:
    ans = 0

    # s>607:sfh
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 608), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 607)))
    ans += wkfl_sfh(temp_ratings)
    
    ans += wkfl_sqq(part_ratings)

    return ans

def wkfl_hl(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2429:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2428)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2429), part_ratings.m.r))
    ans += temp_ratings.total
    
    # m<2450:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2449)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2450), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s>2366:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2367), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2366)))
    
    ans += part_ratings.total

    return ans

def wkfl_hct(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2831:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2832), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2831)))
    
    # x>2514:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2515), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2514)))
    ans += temp_ratings.total

    return ans

def wkfl_phh(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1599:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1600), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1599)))
    ans += temp_ratings.total
    
    ans += wkfl_fmv(part_ratings)

    return ans

def wkfl_lzk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2826:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2825)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2826), part_ratings.s.r))
    ans += temp_ratings.total
    
    # m>3497:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3498), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3497)))
    
    ans += part_ratings.total

    return ans

def wkfl_bp(part_ratings: PartRatings) -> int:
    ans = 0

    # x<381:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 380)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 381), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += wkfl_rl(part_ratings)

    return ans

def wkfl_zfj(part_ratings: PartRatings) -> int:
    ans = 0

    # s>799:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 800), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 799)))

    return ans

def wkfl_grj(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2590:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2589)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2590), part_ratings.a.r))
    ans += temp_ratings.total
    
    # m>3601:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3602), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3601)))
    ans += temp_ratings.total
    
    ans += wkfl_lzk(part_ratings)

    return ans

def wkfl_crh(part_ratings: PartRatings) -> int:
    ans = 0

    # a>415:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 416), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 415)))

    return ans

def wkfl_ddq(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1675:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1674)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1675), part_ratings.s.r))
    
    # m>1049:clt
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1050), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1049)))
    ans += wkfl_clt(temp_ratings)
    
    # a<492:tx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 491)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 492), part_ratings.a.r))
    ans += wkfl_tx(temp_ratings)

    return ans

def wkfl_gg(part_ratings: PartRatings) -> int:
    ans = 0

    # s<195:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 194)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 195), part_ratings.s.r))
    ans += temp_ratings.total
    
    # a<3334:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3333)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3334), part_ratings.a.r))
    ans += temp_ratings.total
    
    # a>3509:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3510), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3509)))
    
    ans += wkfl_td(part_ratings)

    return ans

def wkfl_rrh(part_ratings: PartRatings) -> int:
    ans = 0

    # a>175:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 176), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 175)))
    
    # s>390:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 391), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 390)))
    ans += temp_ratings.total
    
    # a<138:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 137)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 138), part_ratings.a.r))
    
    ans += part_ratings.total

    return ans

def wkfl_bqt(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1637:bd
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1638), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1637)))
    ans += wkfl_bd(temp_ratings)
    
    ans += wkfl_kqc(part_ratings)

    return ans

def wkfl_nbz(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1655:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1654)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1655), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_gh(part_ratings: PartRatings) -> int:
    ans = 0

    # a<309:nl
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 308)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 309), part_ratings.a.r))
    ans += wkfl_nl(temp_ratings)
    
    ans += wkfl_pgr(part_ratings)

    return ans

def wkfl_jsk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1160:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1159)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1160), part_ratings.s.r))

    return ans

def wkfl_fb(part_ratings: PartRatings) -> int:
    ans = 0

    # m>970:lq
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 971), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 970)))
    ans += wkfl_lq(temp_ratings)
    
    ans += wkfl_vrm(part_ratings)

    return ans

def wkfl_qm(part_ratings: PartRatings) -> int:
    ans = 0

    # s>3780:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3781), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3780)))
    
    # m>2873:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2874), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2873)))
    ans += temp_ratings.total

    return ans

def wkfl_rp(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2253:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2252)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2253), part_ratings.s.r))
    
    # x>3049:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3050), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3049)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_xj(part_ratings: PartRatings) -> int:
    ans = 0

    # x>463:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 464), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 463)))
    ans += temp_ratings.total

    return ans

def wkfl_pcx(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1634:jlk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1635), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1634)))
    ans += wkfl_jlk(temp_ratings)
    
    ans += wkfl_hk(part_ratings)

    return ans

def wkfl_dg(part_ratings: PartRatings) -> int:
    ans = 0

    # a<507:kkr
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 506)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 507), part_ratings.a.r))
    ans += wkfl_kkr(temp_ratings)
    
    # s<1701:knx
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1700)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1701), part_ratings.s.r))
    ans += wkfl_knx(temp_ratings)
    
    # m<2153:nh
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2152)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2153), part_ratings.m.r))
    ans += wkfl_nh(temp_ratings)
    
    ans += wkfl_ng(part_ratings)

    return ans

def wkfl_pgr(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1402:dhr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1401)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1402), part_ratings.s.r))
    ans += wkfl_dhr(temp_ratings)
    
    # x<1539:cgz
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1538)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1539), part_ratings.x.r))
    ans += wkfl_cgz(temp_ratings)
    
    # m>1479:hsz
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1480), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1479)))
    ans += wkfl_hsz(temp_ratings)
    
    ans += wkfl_zcd(part_ratings)

    return ans

def wkfl_dft(part_ratings: PartRatings) -> int:
    ans = 0

    # x>894:dv
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 895), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 894)))
    ans += wkfl_dv(temp_ratings)
    
    # a>1914:tb
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1915), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1914)))
    ans += wkfl_tb(temp_ratings)
    
    # a>1752:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1753), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1752)))
    
    ans += part_ratings.total

    return ans

def wkfl_gvb(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3246:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3245)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3246), part_ratings.a.r))
    ans += temp_ratings.total
    
    # x<897:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 896)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 897), part_ratings.x.r))
    ans += temp_ratings.total
    
    # x<1036:mh
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1035)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1036), part_ratings.x.r))
    ans += wkfl_mh(temp_ratings)
    
    ans += wkfl_bg(part_ratings)

    return ans

def wkfl_gm(part_ratings: PartRatings) -> int:
    ans = 0

    # s>3232:gvb
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3233), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3232)))
    ans += wkfl_gvb(temp_ratings)
    
    # x<862:htj
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 861)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 862), part_ratings.x.r))
    ans += wkfl_htj(temp_ratings)
    
    # a<3394:dtm
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3393)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3394), part_ratings.a.r))
    ans += wkfl_dtm(temp_ratings)
    
    ans += wkfl_xrs(part_ratings)

    return ans

def wkfl_bjr(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1239:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1240), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1239)))
    
    ans += part_ratings.total

    return ans

def wkfl_xqj(part_ratings: PartRatings) -> int:
    ans = 0

    # s<591:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 590)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 591), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_hs(part_ratings: PartRatings) -> int:
    ans = 0

    # a<101:pfn
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 100)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 101), part_ratings.a.r))
    ans += wkfl_pfn(temp_ratings)
    
    ans += wkfl_fb(part_ratings)

    return ans

def wkfl_bx(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2203:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2202)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2203), part_ratings.x.r))
    ans += temp_ratings.total
    
    # m>525:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 526), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 525)))
    ans += temp_ratings.total
    
    # a<3797:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3796)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3797), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_rgn(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2544:dc
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2543)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2544), part_ratings.m.r))
    ans += wkfl_dc(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_dtp(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2907:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2906)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2907), part_ratings.s.r))
    
    # a<1367:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1366)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1367), part_ratings.a.r))
    ans += temp_ratings.total
    
    # s<3356:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3355)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3356), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_xrs(part_ratings: PartRatings) -> int:
    ans = 0

    # m<3218:zs
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3217)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3218), part_ratings.m.r))
    ans += wkfl_zs(temp_ratings)
    
    ans += wkfl_kbh(part_ratings)

    return ans

def wkfl_pbd(part_ratings: PartRatings) -> int:
    ans = 0

    # x<767:rdk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 766)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 767), part_ratings.x.r))
    ans += wkfl_rdk(temp_ratings)
    
    # a>1955:xqj
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1956), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1955)))
    ans += wkfl_xqj(temp_ratings)

    return ans

def wkfl_jk(part_ratings: PartRatings) -> int:
    ans = 0

    # x>475:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 476), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 475)))
    ans += temp_ratings.total
    
    # m>735:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 736), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 735)))
    
    ans += part_ratings.total

    return ans

def wkfl_jkd(part_ratings: PartRatings) -> int:
    ans = 0

    # s>382:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 383), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 382)))
    ans += temp_ratings.total

    return ans

def wkfl_jdj(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1069:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1070), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1069)))
    
    # x<2063:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2062)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2063), part_ratings.x.r))
    
    # m>1449:jft
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1450), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1449)))
    ans += wkfl_jft(temp_ratings)

    return ans

def wkfl_sh(part_ratings: PartRatings) -> int:
    ans = 0

    # s>973:qtg
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 974), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 973)))
    ans += wkfl_qtg(temp_ratings)
    
    # a<3299:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3298)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3299), part_ratings.a.r))
    
    # s>843:njp
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 844), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 843)))
    ans += wkfl_njp(temp_ratings)

    return ans

def wkfl_mx(part_ratings: PartRatings) -> int:
    ans = 0

    # m<782:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 781)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 782), part_ratings.m.r))
    
    # a>1233:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1234), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1233)))
    
    ans += part_ratings.total

    return ans

def wkfl_rz(part_ratings: PartRatings) -> int:
    ans = 0

    # m>148:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 149), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 148)))
    ans += temp_ratings.total

    return ans

def wkfl_hv(part_ratings: PartRatings) -> int:
    ans = 0

    # a>581:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 582), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 581)))
    ans += temp_ratings.total
    
    # m<1097:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1096)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1097), part_ratings.m.r))
    
    # x>1545:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1546), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1545)))

    return ans

def wkfl_tv(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1402:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1403), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1402)))
    
    # s>1132:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1133), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1132)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_fmv(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3156:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3155)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3156), part_ratings.a.r))
    ans += temp_ratings.total
    
    # s>2817:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2818), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2817)))
    
    # a>3300:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3301), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3300)))
    ans += temp_ratings.total

    return ans

def wkfl_xtp(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3299:zr
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3300), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3299)))
    ans += wkfl_zr(temp_ratings)
    
    ans += wkfl_rn(part_ratings)

    return ans

def wkfl_fsf(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1065:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1066), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1065)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_vb(part_ratings: PartRatings) -> int:
    ans = 0

    # m<902:jk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 901)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 902), part_ratings.m.r))
    ans += wkfl_jk(temp_ratings)
    
    # x<441:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 440)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 441), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += wkfl_stj(part_ratings)

    return ans

def wkfl_fv(part_ratings: PartRatings) -> int:
    ans = 0

    # s<804:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 803)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 804), part_ratings.s.r))

    return ans

def wkfl_nsh(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1820:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1821), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1820)))
    
    ans += part_ratings.total

    return ans

def wkfl_tsq(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1368:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1367)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1368), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_kbh(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3711:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3712), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3711)))
    
    ans += part_ratings.total

    return ans

def wkfl_ppv(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1487:qpn
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1486)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1487), part_ratings.m.r))
    ans += wkfl_qpn(temp_ratings)
    
    # m<2624:lsr
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2623)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2624), part_ratings.m.r))
    ans += wkfl_lsr(temp_ratings)
    
    ans += wkfl_pk(part_ratings)

    return ans

def wkfl_lth(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2336:czd
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2335)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2336), part_ratings.m.r))
    ans += wkfl_czd(temp_ratings)
    
    ans += wkfl_kvl(part_ratings)

    return ans

def wkfl_ct(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2007:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2006)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2007), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_ppr(part_ratings: PartRatings) -> int:
    ans = 0

    # a>348:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 349), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 348)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_qzr(part_ratings: PartRatings) -> int:
    ans = 0

    # a>217:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 218), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 217)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_blb(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1814:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1813)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1814), part_ratings.x.r))
    ans += temp_ratings.total
    
    # a>909:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 910), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 909)))
    ans += temp_ratings.total
    
    # m<331:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 330)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 331), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += wkfl_blk(part_ratings)

    return ans

def wkfl_vqg(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2587:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2586)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2587), part_ratings.x.r))
    ans += temp_ratings.total
    
    # x>2754:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2755), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2754)))
    ans += temp_ratings.total

    return ans

def wkfl_nbm(part_ratings: PartRatings) -> int:
    ans = 0

    # x<3693:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3692)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3693), part_ratings.x.r))
    
    # x>3858:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3859), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3858)))
    ans += temp_ratings.total
    
    # m<1530:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1529)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1530), part_ratings.m.r))
    ans += temp_ratings.total

    return ans

def wkfl_cx(part_ratings: PartRatings) -> int:
    ans = 0

    # m>986:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 987), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 986)))
    
    # m<723:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 722)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 723), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s<3404:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3403)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3404), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_kmf(part_ratings: PartRatings) -> int:
    ans = 0

    # a<709:st
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 708)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 709), part_ratings.a.r))
    ans += wkfl_st(temp_ratings)
    
    # s>1159:ccj
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1160), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1159)))
    ans += wkfl_ccj(temp_ratings)
    
    # x<1726:cz
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1725)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1726), part_ratings.x.r))
    ans += wkfl_cz(temp_ratings)
    
    ans += wkfl_dx(part_ratings)

    return ans

def wkfl_ts(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2444:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2445), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2444)))
    
    # a>1139:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1140), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1139)))
    ans += temp_ratings.total
    
    # a>383:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 384), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 383)))

    return ans

def wkfl_fp(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1549:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1550), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1549)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_dk(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2698:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2697)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2698), part_ratings.m.r))
    ans += temp_ratings.total
    
    # x<2449:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2448)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2449), part_ratings.x.r))
    
    # s>3326:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3327), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3326)))
    ans += temp_ratings.total

    return ans

def wkfl_hhr(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1749:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1748)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1749), part_ratings.x.r))
    ans += temp_ratings.total
    
    # m>547:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 548), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 547)))

    return ans

def wkfl_lsv(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2400:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2399)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2400), part_ratings.x.r))
    ans += temp_ratings.total
    
    # m>1615:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1616), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1615)))
    ans += temp_ratings.total
    
    # m>1467:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1468), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1467)))
    
    ans += part_ratings.total

    return ans

def wkfl_jlk(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1130:tr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1129)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1130), part_ratings.s.r))
    ans += wkfl_tr(temp_ratings)
    
    # a>3233:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3234), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3233)))
    ans += temp_ratings.total
    
    # s>1532:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1533), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1532)))
    ans += temp_ratings.total
    
    ans += wkfl_fg(part_ratings)

    return ans

def wkfl_cg(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1183:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1184), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1183)))
    
    ans += part_ratings.total

    return ans

def wkfl_srr(part_ratings: PartRatings) -> int:
    ans = 0

    # a>485:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 486), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 485)))
    
    # s<2618:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2617)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2618), part_ratings.s.r))
    ans += temp_ratings.total
    
    # a<252:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 251)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 252), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += wkfl_mxc(part_ratings)

    return ans

def wkfl_kvg(part_ratings: PartRatings) -> int:
    ans = 0

    # m>35:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 36), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 35)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_jfc(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1005:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1004)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1005), part_ratings.s.r))
    ans += temp_ratings.total
    
    # x<1825:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1824)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1825), part_ratings.x.r))
    
    # m<560:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 559)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 560), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_cnq(part_ratings: PartRatings) -> int:
    ans = 0

    # m>428:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 429), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 428)))
    ans += temp_ratings.total
    
    # s>1163:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1164), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1163)))
    
    # a<116:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 115)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 116), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_zmr(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2411:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2410)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2411), part_ratings.m.r))
    
    # a>131:bpr
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 132), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 131)))
    ans += wkfl_bpr(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_xrx(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2375:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2376), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2375)))
    
    # x>3390:hnf
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3391), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3390)))
    ans += wkfl_hnf(temp_ratings)

    return ans

def wkfl_xd(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2074:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2073)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2074), part_ratings.s.r))
    
    # s>2301:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2302), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2301)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_rl(part_ratings: PartRatings) -> int:
    ans = 0

    # x>493:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 494), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 493)))
    
    # x<451:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 450)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 451), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_kq(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2435:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2434)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2435), part_ratings.x.r))
    
    # s<3612:zbz
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3611)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3612), part_ratings.s.r))
    ans += wkfl_zbz(temp_ratings)
    
    # s<3796:xs
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3795)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3796), part_ratings.s.r))
    ans += wkfl_xs(temp_ratings)

    return ans

def wkfl_cjc(part_ratings: PartRatings) -> int:
    ans = 0

    # m>746:pcx
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 747), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 746)))
    ans += wkfl_pcx(temp_ratings)
    
    # a<3205:qmx
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3204)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3205), part_ratings.a.r))
    ans += wkfl_qmx(temp_ratings)
    
    ans += wkfl_tlp(part_ratings)

    return ans

def wkfl_md(part_ratings: PartRatings) -> int:
    ans = 0

    # m<499:lhl
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 498)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 499), part_ratings.m.r))
    ans += wkfl_lhl(temp_ratings)
    
    # a>2683:hcs
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2684), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2683)))
    ans += wkfl_hcs(temp_ratings)
    
    # m>805:mt
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 806), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 805)))
    ans += wkfl_mt(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_gt(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3090:ljj
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3089)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3090), part_ratings.s.r))
    ans += wkfl_ljj(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_jp(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2291:fp
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2292), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2291)))
    ans += wkfl_fp(temp_ratings)
    
    ans += wkfl_ds(part_ratings)

    return ans

def wkfl_gc(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1185:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1184)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1185), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s<3658:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3657)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3658), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s<3806:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3805)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3806), part_ratings.s.r))

    return ans

def wkfl_hx(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1399:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1400), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1399)))
    ans += temp_ratings.total
    
    ans += wkfl_cvn(part_ratings)

    return ans

def wkfl_pqq(part_ratings: PartRatings) -> int:
    ans = 0

    # s<233:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 232)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 233), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_zlc(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2517:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2518), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2517)))
    
    # m<3848:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3847)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3848), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s>2506:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2507), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2506)))
    
    ans += part_ratings.total

    return ans

def wkfl_bvh(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2874:zml
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2875), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2874)))
    ans += wkfl_zml(temp_ratings)
    
    # s<2987:ckd
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2986)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2987), part_ratings.s.r))
    ans += wkfl_ckd(temp_ratings)
    
    # a<1871:cf
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1870)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1871), part_ratings.a.r))
    ans += wkfl_cf(temp_ratings)
    
    ans += wkfl_mbh(part_ratings)

    return ans

def wkfl_xt(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1365:tnd
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1364)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1365), part_ratings.a.r))
    ans += wkfl_tnd(temp_ratings)
    
    # x<1659:vrj
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1658)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1659), part_ratings.x.r))
    ans += wkfl_vrj(temp_ratings)
    
    # s<1095:sxn
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1094)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1095), part_ratings.s.r))
    ans += wkfl_sxn(temp_ratings)
    
    ans += wkfl_hxc(part_ratings)

    return ans

def wkfl_lkb(part_ratings: PartRatings) -> int:
    ans = 0

    # a<831:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 830)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 831), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_qmx(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1392:fzf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1393), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1392)))
    ans += wkfl_fzf(temp_ratings)
    
    # m<385:xtn
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 384)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 385), part_ratings.m.r))
    ans += wkfl_xtn(temp_ratings)
    
    ans += wkfl_jmf(part_ratings)

    return ans

def wkfl_kvl(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2180:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2181), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2180)))
    
    ans += wkfl_xgl(part_ratings)

    return ans

def wkfl_hk(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1029:crj
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1030), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1029)))
    ans += wkfl_crj(temp_ratings)
    
    # x<897:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 896)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 897), part_ratings.x.r))
    
    # x>1308:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1309), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1308)))
    ans += temp_ratings.total
    
    ans += wkfl_tv(part_ratings)

    return ans

def wkfl_zml(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2651:dl
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2652), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2651)))
    ans += wkfl_dl(temp_ratings)
    
    ans += wkfl_xpd(part_ratings)

    return ans

def wkfl_clt(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1718:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1719), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1718)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_lsf(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1350:rlg
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1351), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1350)))
    ans += wkfl_rlg(temp_ratings)

    return ans

def wkfl_fdr(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3361:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3362), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3361)))
    
    # m>3132:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3133), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3132)))
    ans += temp_ratings.total
    
    # x<654:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 653)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 654), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_rs(part_ratings: PartRatings) -> int:
    ans = 0

    # m>835:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 836), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 835)))
    ans += temp_ratings.total
    
    # a<920:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 919)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 920), part_ratings.a.r))
    ans += temp_ratings.total
    
    # a<1026:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1025)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1026), part_ratings.a.r))

    return ans

def wkfl_cbx(part_ratings: PartRatings) -> int:
    ans = 0

    # a>446:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 447), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 446)))
    ans += temp_ratings.total
    
    # a<405:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 404)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 405), part_ratings.a.r))
    ans += temp_ratings.total
    
    # x>1386:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1387), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1386)))

    return ans

def wkfl_sx(part_ratings: PartRatings) -> int:
    ans = 0

    # a<174:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 173)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 174), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_jcq(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2321:cnv
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2322), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2321)))
    ans += wkfl_cnv(temp_ratings)
    
    # s<1630:pz
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1629)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1630), part_ratings.s.r))
    ans += wkfl_pz(temp_ratings)
    
    # x>1538:dg
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1539), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1538)))
    ans += wkfl_dg(temp_ratings)
    
    ans += wkfl_mz(part_ratings)

    return ans

def wkfl_hr(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1519:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1520), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1519)))

    return ans

def wkfl_hc(part_ratings: PartRatings) -> int:
    ans = 0

    # x<369:rbc
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 368)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 369), part_ratings.x.r))
    ans += wkfl_rbc(temp_ratings)
    
    ans += wkfl_cjz(part_ratings)

    return ans

def wkfl_vl(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2539:vmk
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2540), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2539)))
    ans += wkfl_vmk(temp_ratings)
    
    ans += wkfl_fdr(part_ratings)

    return ans

def wkfl_sz(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3350:ktp
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3351), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3350)))
    ans += wkfl_ktp(temp_ratings)
    
    # m>2889:hpq
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2890), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2889)))
    ans += wkfl_hpq(temp_ratings)
    
    ans += wkfl_pl(part_ratings)

    return ans

def wkfl_fn(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1110:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1111), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1110)))
    
    # s<1035:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1034)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1035), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s<1063:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1062)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1063), part_ratings.s.r))

    return ans

def wkfl_cq(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1362:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1363), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1362)))
    ans += temp_ratings.total
    
    # a<1568:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1567)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1568), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_bg(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3545:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3544)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3545), part_ratings.a.r))
    
    # a>3798:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3799), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3798)))
    
    # a<3713:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3712)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3713), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_htj(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2418:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2419), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2418)))
    ans += temp_ratings.total
    
    # m>3061:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3062), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3061)))
    ans += temp_ratings.total
    
    ans += wkfl_qs(part_ratings)

    return ans

def wkfl_jbp(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2646:md
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2645)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2646), part_ratings.x.r))
    ans += wkfl_md(temp_ratings)
    
    ans += wkfl_cc(part_ratings)

    return ans

def wkfl_st(part_ratings: PartRatings) -> int:
    ans = 0

    # a>564:znc
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 565), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 564)))
    ans += wkfl_znc(temp_ratings)
    
    # s<1257:gd
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1256)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1257), part_ratings.s.r))
    ans += wkfl_gd(temp_ratings)
    
    ans += wkfl_zct(part_ratings)

    return ans

def wkfl_kpg(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2688:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2689), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2688)))
    
    # m<3392:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3391)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3392), part_ratings.m.r))
    ans += temp_ratings.total
    
    # a<2491:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2490)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2491), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_fsk(part_ratings: PartRatings) -> int:
    ans = 0

    # m>357:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 358), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 357)))
    ans += temp_ratings.total
    
    # m<311:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 310)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 311), part_ratings.m.r))
    ans += temp_ratings.total
    
    # x<3129:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3128)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3129), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_jbm(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2382:ntr
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2383), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2382)))
    ans += wkfl_ntr(temp_ratings)
    
    # x>1828:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1829), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1828)))
    ans += temp_ratings.total
    
    # s>174:ck
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 175), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 174)))
    ans += wkfl_ck(temp_ratings)

    return ans

def wkfl_ps(part_ratings: PartRatings) -> int:
    ans = 0

    # s<431:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 430)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 431), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s>747:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 748), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 747)))
    ans += temp_ratings.total
    
    # a>936:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 937), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 936)))

    return ans

def wkfl_rpf(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2575:tfn
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2574)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2575), part_ratings.s.r))
    ans += wkfl_tfn(temp_ratings)
    
    # a>3276:bfh
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3277), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3276)))
    ans += wkfl_bfh(temp_ratings)
    
    # x>2664:gp
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2665), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2664)))
    ans += wkfl_gp(temp_ratings)
    
    ans += wkfl_vm(part_ratings)

    return ans

def wkfl_ftx(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1690:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1691), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1690)))
    ans += temp_ratings.total
    
    # m>794:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 795), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 794)))
    
    # a<817:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 816)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 817), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_hm(part_ratings: PartRatings) -> int:
    ans = 0

    # s<527:tkq
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 526)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 527), part_ratings.s.r))
    ans += wkfl_tkq(temp_ratings)
    
    ans += wkfl_vg(part_ratings)

    return ans

def wkfl_tq(part_ratings: PartRatings) -> int:
    ans = 0

    # s>559:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 560), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 559)))
    
    # s<257:df
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 256)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 257), part_ratings.s.r))
    ans += wkfl_df(temp_ratings)
    
    ans += wkfl_zdc(part_ratings)

    return ans

def wkfl_gtk(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1751:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1752), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1751)))
    
    # x<258:ggg
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 257)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 258), part_ratings.x.r))
    ans += wkfl_ggg(temp_ratings)
    
    # s<1506:bz
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1505)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1506), part_ratings.s.r))
    ans += wkfl_bz(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_jr(part_ratings: PartRatings) -> int:
    ans = 0

    # m<842:vc
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 841)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 842), part_ratings.m.r))
    ans += wkfl_vc(temp_ratings)
    
    ans += wkfl_np(part_ratings)

    return ans

def wkfl_mn(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3484:qzr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3483)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3484), part_ratings.s.r))
    ans += wkfl_qzr(temp_ratings)
    
    # a<221:bb
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 220)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 221), part_ratings.a.r))
    ans += wkfl_bb(temp_ratings)
    
    ans += wkfl_qc(part_ratings)

    return ans

def wkfl_blk(part_ratings: PartRatings) -> int:
    ans = 0

    # a>796:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 797), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 796)))
    ans += temp_ratings.total
    
    # s<1618:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1617)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1618), part_ratings.s.r))
    
    # a>736:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 737), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 736)))

    return ans

def wkfl_zb(part_ratings: PartRatings) -> int:
    ans = 0

    # x<3229:xtz
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3228)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3229), part_ratings.x.r))
    ans += wkfl_xtz(temp_ratings)
    
    ans += wkfl_kgc(part_ratings)

    return ans

def wkfl_hhp(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1773:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1772)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1773), part_ratings.m.r))
    ans += temp_ratings.total
    
    # x<3131:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3130)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3131), part_ratings.x.r))
    
    ans += part_ratings.total

    return ans

def wkfl_xtq(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2186:nz
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2187), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2186)))
    ans += wkfl_nz(temp_ratings)
    
    # x<1290:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1289)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1290), part_ratings.x.r))

    return ans

def wkfl_bdm(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2036:shf
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2035)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2036), part_ratings.x.r))
    ans += wkfl_shf(temp_ratings)

    return ans

def wkfl_rlg(part_ratings: PartRatings) -> int:
    ans = 0

    # s<684:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 683)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 684), part_ratings.s.r))
    ans += temp_ratings.total
    
    # m<875:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 874)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 875), part_ratings.m.r))
    
    # m<1631:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1630)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1631), part_ratings.m.r))
    ans += temp_ratings.total

    return ans

def wkfl_dv(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2197:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2196)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2197), part_ratings.a.r))
    
    # s>2537:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2538), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2537)))
    ans += temp_ratings.total
    
    # a<2331:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2330)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2331), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_bd(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1013:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1014), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1013)))
    
    # x>242:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 243), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 242)))
    ans += temp_ratings.total

    return ans

def wkfl_lq(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1354:sx
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1355), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1354)))
    ans += wkfl_sx(temp_ratings)
    
    # s>720:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 721), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 720)))
    ans += temp_ratings.total
    
    ans += wkfl_rrh(part_ratings)

    return ans

def wkfl_fq(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1264:hv
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1265), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1264)))
    ans += wkfl_hv(temp_ratings)
    
    # m>1131:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1132), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1131)))
    ans += temp_ratings.total
    
    ans += wkfl_tp(part_ratings)

    return ans

def wkfl_gs(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1566:ns
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1567), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1566)))
    ans += wkfl_ns(temp_ratings)
    
    ans += wkfl_vfj(part_ratings)

    return ans

def wkfl_cnv(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1602:qsp
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1601)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1602), part_ratings.s.r))
    ans += wkfl_qsp(temp_ratings)
    
    # m<2380:ddq
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2379)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2380), part_ratings.m.r))
    ans += wkfl_ddq(temp_ratings)
    
    ans += wkfl_ngr(part_ratings)

    return ans

def wkfl_xm(part_ratings: PartRatings) -> int:
    ans = 0

    # m<343:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 342)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 343), part_ratings.m.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_mmh(part_ratings: PartRatings) -> int:
    ans = 0

    # s<291:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 290)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 291), part_ratings.s.r))
    
    # x<1456:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1455)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1456), part_ratings.x.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_zms(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2039:lsv
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2038)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2039), part_ratings.a.r))
    ans += wkfl_lsv(temp_ratings)
    
    # a>2233:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2234), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2233)))
    
    ans += part_ratings.total

    return ans

def wkfl_xp(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3844:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3845), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3844)))
    
    # m<3838:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3837)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3838), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s<2189:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2188)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2189), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_rtf(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1523:nf
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1524), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1523)))
    ans += wkfl_nf(temp_ratings)

    return ans

def wkfl_zc(part_ratings: PartRatings) -> int:
    ans = 0

    # a>3480:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3481), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3480)))
    
    # x<2433:tnt
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2432)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2433), part_ratings.x.r))
    ans += wkfl_tnt(temp_ratings)
    
    # s<3567:crr
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3566)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3567), part_ratings.s.r))
    ans += wkfl_crr(temp_ratings)
    
    ans += wkfl_qm(part_ratings)

    return ans

def wkfl_vcf(part_ratings: PartRatings) -> int:
    ans = 0

    # s>1064:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1065), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1064)))
    
    # m<1393:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1392)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1393), part_ratings.m.r))
    
    # x<3004:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3003)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3004), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_hjl(part_ratings: PartRatings) -> int:
    ans = 0

    # x<877:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 876)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 877), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_hgb(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2627:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2626)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2627), part_ratings.a.r))
    
    # m>2929:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2930), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2929)))
    ans += temp_ratings.total
    
    # x>3373:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 3374), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 3373)))
    ans += temp_ratings.total

    return ans

def wkfl_xqq(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1122:zpn
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1121)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1122), part_ratings.x.r))
    ans += wkfl_zpn(temp_ratings)
    
    ans += wkfl_knn(part_ratings)

    return ans

def wkfl_hpq(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1358:czz
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1357)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1358), part_ratings.a.r))
    ans += wkfl_czz(temp_ratings)
    
    # a<2378:cnl
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2377)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2378), part_ratings.a.r))
    ans += wkfl_cnl(temp_ratings)
    
    ans += wkfl_kn(part_ratings)

    return ans

def wkfl_dn(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2817:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2816)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2817), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s>955:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 956), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 955)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_cf(part_ratings: PartRatings) -> int:
    ans = 0

    # a>676:xtp
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 677), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 676)))
    ans += wkfl_xtp(temp_ratings)
    
    # a>429:cd
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 430), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 429)))
    ans += wkfl_cd(temp_ratings)
    
    # a>284:krj
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 285), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 284)))
    ans += wkfl_krj(temp_ratings)
    
    ans += wkfl_hrs(part_ratings)

    return ans

def wkfl_rbc(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2943:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2944), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2943)))
    ans += temp_ratings.total
    
    # a<3139:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3138)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3139), part_ratings.a.r))
    
    # s>2207:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2208), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2207)))

    return ans

def wkfl_hzs(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1005:km
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1004)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1005), part_ratings.s.r))
    ans += wkfl_km(temp_ratings)
    
    # a<777:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 776)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 777), part_ratings.a.r))
    
    # m>1999:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2000), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1999)))
    ans += temp_ratings.total

    return ans

def wkfl_snd(part_ratings: PartRatings) -> int:
    ans = 0

    # x<2160:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2159)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2160), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_pts(part_ratings: PartRatings) -> int:
    ans = 0

    # s>910:qx
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 911), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 910)))
    ans += wkfl_qx(temp_ratings)
    
    ans += wkfl_pbd(part_ratings)

    return ans

def wkfl_pr(part_ratings: PartRatings) -> int:
    ans = 0

    # x>496:ps
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 497), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 496)))
    ans += wkfl_ps(temp_ratings)
    
    # s<622:gn
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 621)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 622), part_ratings.s.r))
    ans += wkfl_gn(temp_ratings)
    
    # x<306:lld
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 305)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 306), part_ratings.x.r))
    ans += wkfl_lld(temp_ratings)
    
    ans += wkfl_zfj(part_ratings)

    return ans

def wkfl_vrb(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2168:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2169), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2168)))
    ans += temp_ratings.total
    
    # x<2939:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2938)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2939), part_ratings.x.r))
    ans += temp_ratings.total
    
    # s<1299:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1298)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1299), part_ratings.s.r))
    
    ans += part_ratings.total

    return ans

def wkfl_fcr(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1992:bvh
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1993), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1992)))
    ans += wkfl_bvh(temp_ratings)
    
    # x<1197:kk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1196)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1197), part_ratings.x.r))
    ans += wkfl_kk(temp_ratings)
    
    ans += wkfl_sz(part_ratings)

    return ans

def wkfl_fd(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3312:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3311)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3312), part_ratings.s.r))
    
    # a>799:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 800), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 799)))
    
    ans += part_ratings.total

    return ans

def wkfl_mt(part_ratings: PartRatings) -> int:
    ans = 0

    # x>1417:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1418), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1417)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_ql(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1450:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1449)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1450), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_dxp(part_ratings: PartRatings) -> int:
    ans = 0

    # m<453:dnn
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 452)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 453), part_ratings.m.r))
    ans += wkfl_dnn(temp_ratings)
    
    # a>2362:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2363), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2362)))

    return ans

def wkfl_qx(part_ratings: PartRatings) -> int:
    ans = 0

    # s<1418:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1417)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1418), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += wkfl_njr(part_ratings)

    return ans

def wkfl_vfj(part_ratings: PartRatings) -> int:
    ans = 0

    # a<2161:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2160)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2161), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_sqf(part_ratings: PartRatings) -> int:
    ans = 0

    # s<443:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 442)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 443), part_ratings.s.r))
    ans += temp_ratings.total
    
    # m>2471:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2472), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2471)))
    ans += temp_ratings.total

    return ans

def wkfl_qhk(part_ratings: PartRatings) -> int:
    ans = 0

    # a<697:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 696)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 697), part_ratings.a.r))
    
    # m<94:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 93)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 94), part_ratings.m.r))
    ans += temp_ratings.total
    
    # s>2770:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2771), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2770)))
    ans += temp_ratings.total

    return ans

def wkfl_khz(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1572:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1573), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1572)))
    ans += temp_ratings.total
    
    # s<2885:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2884)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2885), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += wkfl_ptz(part_ratings)

    return ans

def wkfl_rrl(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2077:nk
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2078), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2077)))
    ans += wkfl_nk(temp_ratings)
    
    # m>578:qcr
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 579), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 578)))
    ans += wkfl_qcr(temp_ratings)
    
    # a>996:sjv
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 997), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 996)))
    ans += wkfl_sjv(temp_ratings)
    
    ans += wkfl_pv(part_ratings)

    return ans

def wkfl_pd(part_ratings: PartRatings) -> int:
    ans = 0

    # s<3893:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3892)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3893), part_ratings.s.r))
    
    # m>48:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 49), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 48)))
    
    # x>1937:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1938), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1937)))

    return ans

def wkfl_hh(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2263:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2264), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2263)))
    
    # s>1964:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1965), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1964)))

    return ans

def wkfl_zdc(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1650:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1649)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1650), part_ratings.a.r))

    return ans

def wkfl_lfz(part_ratings: PartRatings) -> int:
    ans = 0

    # s>766:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 767), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 766)))
    ans += temp_ratings.total
    
    # m>1252:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1253), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1252)))
    ans += temp_ratings.total
    
    ans += wkfl_szx(part_ratings)

    return ans

def wkfl_snc(part_ratings: PartRatings) -> int:
    ans = 0

    # x<510:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 509)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 510), part_ratings.x.r))
    ans += temp_ratings.total
    
    # a<758:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 757)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 758), part_ratings.a.r))
    ans += temp_ratings.total
    
    # a<783:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 782)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 783), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_lrv(part_ratings: PartRatings) -> int:
    ans = 0

    # s>2792:zzc
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2793), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2792)))
    ans += wkfl_zzc(temp_ratings)
    
    # s<2399:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2398)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2399), part_ratings.s.r))
    
    # m>919:xcs
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 920), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 919)))
    ans += wkfl_xcs(temp_ratings)

    return ans

def wkfl_cbp(part_ratings: PartRatings) -> int:
    ans = 0

    # a>973:R
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 974), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 973)))
    
    # m>1397:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1398), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1397)))
    
    # s>454:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 455), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 454)))
    
    ans += part_ratings.total

    return ans

def wkfl_ghz(part_ratings: PartRatings) -> int:
    ans = 0

    # a>113:hqb
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 114), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 113)))
    ans += wkfl_hqb(temp_ratings)
    
    # x>2596:qnd
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2597), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2596)))
    ans += wkfl_qnd(temp_ratings)
    
    ans += wkfl_fs(part_ratings)

    return ans

def wkfl_bpj(part_ratings: PartRatings) -> int:
    ans = 0

    # a<809:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 808)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 809), part_ratings.a.r))
    ans += temp_ratings.total
    
    # s<1088:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1087)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1088), part_ratings.s.r))
    
    # x>1033:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1034), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1033)))
    ans += temp_ratings.total

    return ans

def wkfl_nm(part_ratings: PartRatings) -> int:
    ans = 0

    # m>1867:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1868), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1867)))
    
    # x<1396:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1395)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1396), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_cm(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1960:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1959)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1960), part_ratings.m.r))
    
    # a<1206:chg
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1205)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1206), part_ratings.a.r))
    ans += wkfl_chg(temp_ratings)
    
    # x>2233:dtp
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2234), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2233)))
    ans += wkfl_dtp(temp_ratings)
    
    ans += wkfl_rj(part_ratings)

    return ans

def wkfl_vv(part_ratings: PartRatings) -> int:
    ans = 0

    # m>3801:A
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 3802), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 3801)))
    ans += temp_ratings.total

    return ans

def wkfl_cr(part_ratings: PartRatings) -> int:
    ans = 0

    # a>1924:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1925), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1924)))
    ans += temp_ratings.total
    
    # a>1850:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1851), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1850)))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_px(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1831:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1830)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1831), part_ratings.x.r))
    ans += temp_ratings.total
    
    # s<2981:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2980)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2981), part_ratings.s.r))
    ans += temp_ratings.total

    return ans

def wkfl_cc(part_ratings: PartRatings) -> int:
    ans = 0

    # m<464:zk
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 463)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 464), part_ratings.m.r))
    ans += wkfl_zk(temp_ratings)
    
    ans += part_ratings.total

    return ans

def wkfl_tr(part_ratings: PartRatings) -> int:
    ans = 0

    # a>2913:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2914), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2913)))
    ans += temp_ratings.total
    
    # s>927:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 928), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 927)))
    ans += temp_ratings.total
    
    # a<2508:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 2507)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 2508), part_ratings.a.r))
    ans += temp_ratings.total

    return ans

def wkfl_rr(part_ratings: PartRatings) -> int:
    ans = 0

    # s<2862:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2861)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2862), part_ratings.s.r))
    ans += temp_ratings.total
    
    # s<3387:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3386)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3387), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_zlj(part_ratings: PartRatings) -> int:
    ans = 0

    # x>2280:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 2281), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 2280)))
    ans += temp_ratings.total
    
    # a>1213:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1214), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1213)))
    ans += temp_ratings.total

    return ans

def wkfl_gvd(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3539:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3538)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3539), part_ratings.a.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans

def wkfl_qdx(part_ratings: PartRatings) -> int:
    ans = 0

    # a<3152:pgj
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3151)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3152), part_ratings.a.r))
    ans += wkfl_pgj(temp_ratings)
    
    # a>3680:xtq
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 3681), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 3680)))
    ans += wkfl_xtq(temp_ratings)
    
    # s<683:db
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 682)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 683), part_ratings.s.r))
    ans += wkfl_db(temp_ratings)
    
    ans += wkfl_kf(part_ratings)

    return ans

def wkfl_rt(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1169:jxs
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1168)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1169), part_ratings.m.r))
    ans += wkfl_jxs(temp_ratings)
    
    # x>1210:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1211), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1210)))
    ans += temp_ratings.total
    
    # a>241:dh
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 242), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 241)))
    ans += wkfl_dh(temp_ratings)
    
    ans += wkfl_bl(part_ratings)

    return ans

def wkfl_fzb(part_ratings: PartRatings) -> int:
    ans = 0

    # a<1909:A
    temp_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1908)))
    part_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1909), part_ratings.a.r))
    ans += temp_ratings.total
    
    # x>1470:lk
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1471), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1470)))
    ans += wkfl_lk(temp_ratings)
    
    # s>2790:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2791), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2790)))
    
    ans += wkfl_xnb(part_ratings)

    return ans

def wkfl_sjv(part_ratings: PartRatings) -> int:
    ans = 0

    # m>240:tqf
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 241), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 240)))
    ans += wkfl_tqf(temp_ratings)
    
    # a>1375:mm
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 1376), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 1375)))
    ans += wkfl_mm(temp_ratings)
    
    # s<2795:tl
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 2794)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 2795), part_ratings.s.r))
    ans += wkfl_tl(temp_ratings)
    
    ans += wkfl_sd(part_ratings)

    return ans

def wkfl_lsr(part_ratings: PartRatings) -> int:
    ans = 0

    # m>2100:vlt
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2101), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2100)))
    ans += wkfl_vlt(temp_ratings)
    
    # a>915:flh
    temp_ratings = dataclasses.replace(part_ratings, a=Range(max(part_ratings.a.l, 916), part_ratings.a.r))
    part_ratings = dataclasses.replace(part_ratings, a=Range(part_ratings.a.l, min(part_ratings.a.r, 915)))
    ans += wkfl_flh(temp_ratings)
    
    ans += wkfl_ktc(part_ratings)

    return ans

def wkfl_nf(part_ratings: PartRatings) -> int:
    ans = 0

    # m<1838:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 1837)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 1838), part_ratings.m.r))
    
    # x>602:R
    temp_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 603), part_ratings.x.r))
    part_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 602)))
    
    # s>1568:R
    temp_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 1569), part_ratings.s.r))
    part_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 1568)))

    return ans

def wkfl_knn(part_ratings: PartRatings) -> int:
    ans = 0

    # x<1325:A
    temp_ratings = dataclasses.replace(part_ratings, x=Range(part_ratings.x.l, min(part_ratings.x.r, 1324)))
    part_ratings = dataclasses.replace(part_ratings, x=Range(max(part_ratings.x.l, 1325), part_ratings.x.r))
    ans += temp_ratings.total

    return ans

def wkfl_hmj(part_ratings: PartRatings) -> int:
    ans = 0

    # m<2476:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2475)))
    part_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2476), part_ratings.m.r))
    
    # m>2543:R
    temp_ratings = dataclasses.replace(part_ratings, m=Range(max(part_ratings.m.l, 2544), part_ratings.m.r))
    part_ratings = dataclasses.replace(part_ratings, m=Range(part_ratings.m.l, min(part_ratings.m.r, 2543)))
    
    # s<3602:A
    temp_ratings = dataclasses.replace(part_ratings, s=Range(part_ratings.s.l, min(part_ratings.s.r, 3601)))
    part_ratings = dataclasses.replace(part_ratings, s=Range(max(part_ratings.s.l, 3602), part_ratings.s.r))
    ans += temp_ratings.total
    
    ans += part_ratings.total

    return ans
