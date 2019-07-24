#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QFileDialog>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    inputLabel = findChild<QLabel*>("inputLabel");
    outputLabel = findChild<QLabel*>("outputLabel");

}


MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_actionCargar_imagen_triggered()
{
    QString fileName = QFileDialog::getOpenFileName(this,
        tr("Cargar imagen"), "", tr("Arquivos de imagem (*.png *.jpg *.bmp)"));

    QImage qImage(fileName);

    if( !qImage.isNull() )
    {
        inputImage.fromQImage(qImage);
        inputLabel->setPixmap(QPixmap::fromImage(qImage));
    }
}


void MainWindow::on_actionSalvar_imagem_triggered()
{
    if( !outputImage.getColorBuffer().empty() )
    {
        QString fileName = QFileDialog::getSaveFileName(this,
        tr("Salvar imagem"), "", tr("Arquivos de imagem (*.png *.jpg *.bmp *.tiff)"));

        if (!fileName.isEmpty() )
        {
            QImage qImage = outputImage.toQImage();
            qImage.save(fileName);
        }
    }
}


void MainWindow::on_actionCarregar_resultado_triggered()
{
    inputImage=outputImage;
    outputImage=Image();
    updateOutputLabel();
    updateInputLabel();
}


void MainWindow::on_actionSmoothing_triggered()
{
    if( !inputImage.getColorBuffer().empty() )
    {
        smoothing(inputImage, outputImage);
        updateOutputLabel();
    }
}


void MainWindow::on_actionArestas_triggered()
{
    if( !inputImage.getColorBuffer().empty() )
    {
        sobel(inputImage, outputImage);
        updateOutputLabel();
    }
}


void MainWindow::on_actionHaar_triggered()
{


    clock_t begin = clock();
      if( !inputImage.getColorBuffer().empty() )
    {
        haar(inputImage, outputImage);
        updateOutputLabel();
    }
     clock_t end = clock();
     double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    cout<<"TIempo requerido:"<<elapsed_secs<<endl;
}


void MainWindow::on_actionHaar_inverso_triggered()
{
    if( !inputImage.getColorBuffer().empty() )
    {
        haarInv(inputImage, outputImage);
        updateOutputLabel();
    }
}


void MainWindow::on_actionRealce_em_Haar_triggered()
{
    if( !outputImage.getColorBuffer().empty() )
    {
        inputImage=outputImage;
        enhanceHaar(inputImage, outputImage);
        updateOutputLabel();
        updateInputLabel();
    }

}


void MainWindow::updateInputLabel()
{
    QImage qImage = inputImage.toQImage();
    inputLabel->setPixmap(QPixmap::fromImage(qImage));
}


void MainWindow::updateOutputLabel()
{
    QImage qImage = outputImage.toQImage();
    outputLabel->setPixmap(QPixmap::fromImage(qImage));
    //qImage.save("Salida.bmp");
    //bool QImage::save ( const QString & fileName, const char * format = 0, int quality = -1 );
}
