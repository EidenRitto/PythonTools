oldword = '"关于"'
javaword = 'MyLanguageConfig.getInfo("About")'

line = '	private JLabel aboutJLabel = new JLabel("关于", JLabel.CENTER);// 关于标题'
print(line.replace(oldword, javaword))
