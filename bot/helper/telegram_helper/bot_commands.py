from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_SUFFIX}'
        self.MirrorCommand = [f'yg{CMD_SUFFIX}', f'ym{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'ygqb{CMD_SUFFIX}', f'yqb{CMD_SUFFIX}']
        self.YtdlCommand = [
            f'ytdl{CMD_SUFFIX}', f'ygy{CMD_SUFFIX}', f'ywatch{CMD_SUFFIX}', f'yw{CMD_SUFFIX}']
        self.LeechCommand = [f'ygleech{CMD_SUFFIX}', f'yl{CMD_SUFFIX}']
        self.QbLeechCommand = [f'ygqbleech{CMD_SUFFIX}', f'yqbl{CMD_SUFFIX}']
        self.YtdlLeechCommand = [
            f'ytdlleech{CMD_SUFFIX}', f'ygyl{CMD_SUFFIX}', f'ywatchleech{CMD_SUFFIX}', f'ywl{CMD_SUFFIX}']
        self.CloneCommand = [f'ygclone{CMD_SUFFIX}', f'ycl{CMD_SUFFIX}']
        self.CountCommand = [f'ygcount{CMD_SUFFIX}', f'yco{CMD_SUFFIX}']
        self.DeleteCommand = [f'ygdelete{CMD_SUFFIX}', f'ydel{CMD_SUFFIX}']
        self.CancelMirror = [f'ygc{CMD_SUFFIX}', f'pc{CMD_SUFFIX}']
        self.CancelAllCommand = [f'ygcancelall{CMD_SUFFIX}', f'yca{CMD_SUFFIX}']
        self.ListCommand = [f'yglist{CMD_SUFFIX}', f'yli{CMD_SUFFIX}']
        self.SearchCommand = [f'ygsearch{CMD_SUFFIX}', f'yse{CMD_SUFFIX}']
        self.StatusCommand = [f'ygstatus{CMD_SUFFIX}', f'ysta{CMD_SUFFIX}']
        self.UsersCommand = [f'ygusers{CMD_SUFFIX}', f'yus{CMD_SUFFIX}']
        self.AuthorizeCommand = [f'ygauthorize{CMD_SUFFIX}', f'yau{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [
            f'unauthorize{CMD_SUFFIX}', f'ygua{CMD_SUFFIX}']
        self.AddSudoCommand = [f'ygaddsudo{CMD_SUFFIX}', f'yas{CMD_SUFFIX}']
        self.RmSudoCommand = [f'ygrmsudo{CMD_SUFFIX}', f'yrs{CMD_SUFFIX}']
        self.PingCommand = [f'ygping{CMD_SUFFIX}', f'yp{CMD_SUFFIX}']
        self.RestartCommand = [f'ygrestart{CMD_SUFFIX}', f'yr{CMD_SUFFIX}']
        self.StatsCommand = [f'ygstats{CMD_SUFFIX}', f'ysts{CMD_SUFFIX}']
        self.HelpCommand = [f'yghelp{CMD_SUFFIX}', f'yh{CMD_SUFFIX}']
        self.LogCommand = [f'yglog{CMD_SUFFIX}', f'ylo{CMD_SUFFIX}']
        self.ShellCommand = [f'ygshell{CMD_SUFFIX}', f'ysh{CMD_SUFFIX}']
        self.SpeedCommand = [f'ygspeedtest{CMD_SUFFIX}', f'ysp{CMD_SUFFIX}']
        self.EvalCommand = [f'ygeval{CMD_SUFFIX}', f'yev{CMD_SUFFIX}']
        self.ExecCommand = [f'ygexec{CMD_SUFFIX}', f'yex{CMD_SUFFIX}']
        self.ClearLocalsCommand = [f'ygclearlocals{CMD_SUFFIX}', f'yclo{CMD_SUFFIX}']
        self.BotSetCommand = [f'ygbsetting{CMD_SUFFIX}', f'ybset{CMD_SUFFIX}']
        self.UserSetCommand = [f'ygusetting{CMD_SUFFIX}', f'yuset{CMD_SUFFIX}']
        self.BtSelectCommand = [f'ygbtsel{CMD_SUFFIX}', f'ybts{CMD_SUFFIX}']
        self.RssCommand = f'ygrss{CMD_SUFFIX}'


BotCommands = _BotCommands()
