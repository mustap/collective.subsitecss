## Script (Python) "customized.css"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=*args, **kwargs
##title=
##
bg = context.get('background_color') or "#eee"
lc = context.get('link_color') or "#205C90"
sfs = context.get('global_menu_fontsize') or '26px'
lfs = context.get('global_menu_large_fontsize') or sfs
lic = int(context.get('global_menu_large_item_count') or 0)

css = """
body {
    background: url(top-bg.png) repeat-x 0 0 %(bg)s;
}
#portal-slinks {
	border-top:1px solid #545454;
	border-bottom:3px solid #545454;
	clear:both;
	margin:0 0 13px;
	text-transform:uppercase;
        text-align: center;
	}

a.internal-link,
a.external-link,
a.mail-link,
a.anchor-link {
    color: %(lc)s;
}

#portal-slinks li a {
    font-size: %(sfs)s;
}

""" % dict(bg=bg, lc=lc, sfs=sfs)

if not lic:
    return css

lw = str(940/lic)+'px'
css += """

%(pla_sel)s {
    font-size: %(lfs)s;
    width: %(lw)s;
    padding: 0;
    margin: 0;
}

%(pl_sel)s {
    border-bottom: 2px solid black;
    margin: 0;
    padding: 0;
}

""" % dict(lfs=lfs, lw=lw,
           pla_sel=',\n'.join(
        ['#portal-slinks li.portalslinks-%s a'%i for i in range(lic)]),
           pl_sel=',\n'.join(
        ['#portal-slinks li.portalslinks-%s'%i for i in range(lic)]),)

return css
