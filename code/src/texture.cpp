/*
 * @Description: 
 * @Version: 1.0
 * @Autor: like
 * @Date: 2022-06-08 10:22:13
 * @LastEditors: like
 * @LastEditTime: 2022-06-08 17:19:11
 */
#include "cvcommon.hpp"

#define TextureIdentifyError   -1
#define TextureIdentified       1
#define TextureIdentifiedFailed 2
/**
 * @brief 对通过图像中心的指定角度 degree 通过的直线求和
 * 
 * 例如：
 *  0 0 1
 *  0 1 0
 *  1 0 0
 * 指定 degree 为 45 时, 该接口返回值为 3
 */
int MatSum(const Mat& img, int degree/*[0, 180)*/)
{

}

int textureIdentify(char* imputImg, float& angle)
{
    // input args assert
    if(imputImg) return TextureIdentifyError;   

    auto hasTexture      = [&]()->bool
    {
        return true;
    };
    auto getTextureAngle = [&]()->float
    {
        return TextureIdentifyError;
    };
 
    if(!hasTexture()) return TextureIdentifiedFailed;
    float ret = getTextureAngle();
    if(TextureIdentifyError == ret) return TextureIdentifyError;
    angle = ret;
    return TextureIdentified;
}

int main()  
{  
    /*Mat image = Mat::zeros(300, 600, CV_8UC3);  
    circle(image, Point(300, 200), 100, Scalar(25, 110, 288),-100);  
    circle(image, Point(400, 200), 100, Scalar(255, 123, 127), -100);  
    imshow("Show Window", image);  
    waitKey(0); */ 
    return 0;  
}  