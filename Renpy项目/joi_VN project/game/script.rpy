define x = Character('轴芯', color="FF8000")
define m = Character('我', color="#FFCE65")
define n = Character('轴伊', color="#9933FF")

label start:

    scene livecg
    with fade

    x "晚安轴宝。"
    m "晚安晚安，大家晚安。"
    "又是一天直播结束。"
    "正当我与轴芯们晚安时。"
    "忽然，时间好像停滞了,只剩“晚安”的弹幕在眼前不断划过。"
    "怎么回事？"
    "可我却发不出声音，眼前只剩一片黑暗。"

    hide livecg
    "意识仿佛失去了支撑点，不断向下坠去。"
    "忽然，身体仿佛被什么柔软的布料接住。"
    "随后，幕布，被拉开了。"

label planet:

    scene bg planet palace
    show star first
    with dissolve

    "映入眼帘的，是只在我的幻想中存在的星空。"
    "在那片星空中站着一个人。"
    "我认识她，这是当然的。"
    "因为她就是我——轴伊joi。"

    show joi me
    m "......"
    n "额，那个，你好，很抱歉把你叫来"
    play music "audio/potato star.mp3"
    m '因为我是"快乐土豆饼"！'
    $ renpy.movie_cutscene("images/star mv.webm")