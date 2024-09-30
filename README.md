# AUTORUN CCMINER

* Ekrana uzun dokunun ve daha fazlasını seçin.
* Ekranı açık tut seçeneğini seçin.

```
termux-setup-storage
```
* Kabul et'e basın.

```
pkg update -y
```
Her sorguya N yazın
```
pkg install proot-distro -y && proot-distro install ubuntu && pkg install nano -y && pkg install wget -y && cd /data/data/com.termux/files/usr/etc && nano profile
```
* İmleci aşağıya doğru hareket ettirin. Son satıra komutu girin
```
proot-distro login ubuntu
```
* ctrl+x ardından kaydetmek için y'ye cevap verin
* Kapatın ve termux'u tekrar açın.

* Adım adım kurulum
```
apt-get update -y && apt-get install git -y && git clone https://github.com/realdizayn/auto && cd ccminer-autorun-x && chmod +x setup.sh && sh setup.sh
```
* Bash.bashrc dosyasını açtıktan sonra enter ile ilk satırı ekleyin, imleci yukarı hareket ettirin ve komutu girin.
- ```run-miner```
* ardından kaydetmek için ctrl+x y yanıtı verin

# Programın daha fazla kullanımı

## Zergpool durumunda, şifre girilmesi ID=ad girilmesini gerektirmez. Sistem bunu otomatik olarak ekleyecektir.
* Madenciliği durdurmak için tuşuna basınCTRL + C
* TAG'ı değiştirmek için şu komutu kullanın:edit-miner
* Kazmayı açmak için şu komutu kullanın:run-miner

* Bağlantı için bir IP eklemek için şu komutu kullanın:add-ip
# CCMINER-AUTORUN-X
